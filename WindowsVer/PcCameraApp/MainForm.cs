using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using AForge.Video;             // AForge.NETライブラリから読込
using AForge.Video.DirectShow;  // AForge.NETライブラリから読込

using OpenCvSharp;
using OpenCvSharp.Extensions;

using Original;
using WMPLib;
using System.Net;

namespace PcCameraApp
{
    public partial class MainForm : Form
    {
        WindowsMediaPlayer _mediaPlayer = new WindowsMediaPlayer();

        // フィールド
        public bool DeviceExist = false;                // デバイス有無
        public FilterInfoCollection videoDevices;       // カメラデバイスの一覧
        public VideoCaptureDevice videoSource = null;   // カメラデバイスから取得した映像

        Mat mat = new Mat(); //比較元画像
        Mat temp = new Mat(); //比較先画像
        Mat output1 = new Mat(); //比較元画像の特徴点出力先
        Mat output2 = new Mat(); //比較先画像の特徴点出力先
        Mat output3 = new Mat(); //DrawMatchesの出力先

        int good_match_length = 0;         //閾値以下の要素数を格納
        int threshold = 500;       //閾値

        AKAZE akaze = AKAZE.Create(); //AKAZEのセットアップ
        KeyPoint[] key_point1;        //比較元画像の特徴点
        KeyPoint[] key_point2;        //比較先画像の特徴点
        Mat descriptor1 = new Mat();  //比較元画像の特徴量
        Mat descriptor2 = new Mat();  //比較先画像の特徴量

        DescriptorMatcher matcher; //マッチング方法
        DMatch[] matches; //特徴量ベクトル同士のマッチング結果を格納する配列

        public MainForm()
        {
            InitializeComponent();
        }

        // Loadイベント（Formの立ち上げ時に実行）
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBoxResult.Visible = false;

            mat = Cv2.ImRead(@"C:\Users\massi\Downloads\one.jpeg");//比較元画像

            //特徴量の検出と特徴量ベクトルの計算
            akaze.DetectAndCompute(mat, null, out key_point1, descriptor1);

            //画像１の特徴点をoutput1に出力
            Cv2.DrawKeypoints(mat, key_point1, output1);
            //Cv2.ImShow("output1", output1);

            Debug.WriteLine("Formのロード開始");
            this.getCameraInfo();
        }

        // カメラ情報の取得
        public void getCameraInfo()
        {
            try
            {
                // 端末で認識しているカメラデバイスの一覧を取得
                videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                comboBoxCameraType.Items.Clear();

                if (videoDevices.Count == 0)
                    throw new ApplicationException();

                foreach (FilterInfo device in videoDevices)
                {
                    // カメラデバイスの一覧をコンボボックスに追加
                    comboBoxCameraType.Items.Add(device.Name);
                    comboBoxCameraType.SelectedIndex = 0;
                    DeviceExist = true;
                }
            }
            catch (ApplicationException)
            {
                DeviceExist = false;
                comboBoxCameraType.Items.Add("Deviceが存在していません。");
            }
        }

        // 開始or停止ボタン
        private void button1_Click(object sender, EventArgs e)
        {
            Debug.WriteLine("ボタンクリック");

            if (buttonStartStop.Text == "開始")
            {
                pictureBoxResult.Visible = true;

                if (DeviceExist)
                {
                    videoSource = new VideoCaptureDevice(videoDevices[comboBoxCameraType.SelectedIndex].MonikerString);
                    videoSource.NewFrame += new NewFrameEventHandler(videoRendering);
                    this.CloseVideoSource();

                    videoSource.Start();

                    buttonStartStop.Text = "停止";
                    timer1.Enabled = true;
                }
                else
                {
                    labelFps.Text = "デバイスが存在していません。";
                }
            }
            else
            {
                if (videoSource.IsRunning)
                {
                    timer1.Enabled = false;
                    this.CloseVideoSource();
                    labelFps.Text = "停止中";
                    buttonStartStop.Text = "開始";

                    pictureBoxResult.Visible = false;
                }
            }
        }
        // 描画処理
        private void videoRendering(object sender, NewFrameEventArgs eventArgs)
        {
            Bitmap img = (Bitmap)eventArgs.Frame.Clone();

            // Debug.WriteLine(DateTime.Now + ":" + "描画更新");
            // Debug.WriteLine(mode);

            try
            {
                //pictureBoxCamera.Image = img;

                temp = BitmapConverter.ToMat(img);//比較先画像

                //特徴量の検出と特徴量ベクトルの計算
                akaze.DetectAndCompute(temp, null, out key_point2, descriptor2);

                //画像２の特徴点をoutput2に出力
                Cv2.DrawKeypoints(temp, key_point2, output2);
                //Cv2.ImShow("output2", output2);

                pictureBoxCamera.Image = BitmapConverter.ToBitmap(output2);

                matcher = DescriptorMatcher.Create("BruteForce");
                matches = matcher.Match(descriptor1, descriptor2);

                //閾値以下の要素数のカウント
                for (int i = 0; i < key_point1.Length && i < key_point2.Length; ++i)
                {
                    if (matches[i].Distance < threshold)
                    {
                        ++good_match_length;
                    }
                }

                DMatch[] good_matches = new DMatch[good_match_length];//閾値以下の要素数で定義

                //good_matchesに格納していく
                int j = 0;
                for (int i = 0; i < key_point1.Length && i < key_point2.Length; ++i)
                {
                    if (matches[i].Distance < threshold)
                    {
                        good_matches[j] = matches[i];
                        ++j;
                    }
                }

                //good_matchesの個数デバッグ表示
                Debug.WriteLine(j);
                Invoke((MethodInvoker)delegate ()
                {
                    labelMatch.Text = j.ToString();
                });

                //類似点の数が多ければチェックボックスの状態に応じて非常停止
                if (j >= 16)
                {
                    //非常停止
                    if (checkBoxStop.Checked == true)
                    {
                        //WebRequest request = WebRequest.Create("https://maker.ifttt.com/trigger/raspberry/with/key/gHPH_xDKR664IVIr2YtRRj6BbQoQi-K0mCowIJCGPF3");
                        //WebResponse response = request.GetResponse();
                    }

                    //アラート音
                    if (checkBoxAlert.Checked == true)
                    {
                        // _mediaPlayer.settings.volume = 20;
                        _mediaPlayer.URL = @"D:\DCIM\app\AkazeAlert\PcCameraApp\Resources\decision1.mp3";
                        _mediaPlayer.controls.play();
                    }
                }

                Cv2.DrawMatches(mat, key_point1, temp, key_point2, good_matches, output3);
                //Cv2.ImShow("output3", output3);

                pictureBoxResult.Image = BitmapConverter.ToBitmap(output3);
            }
            catch
            {
                pictureBoxCamera.Image = img;
            }
        }
        // 停止の初期化
        private void CloseVideoSource()
        {
            if (!(videoSource == null))
                if (videoSource.IsRunning)
                {
                    videoSource.SignalToStop();
                    videoSource = null;
                }
        }
        // フレームレートの取得
        private void timer1_Tick(object sender, EventArgs e)
        {
            labelFps.Text = videoSource.FramesReceived.ToString() + "FPS";
        }
        // ソフト終了時のクローズ処理
        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (videoSource != null)
            {
                // Form を閉じる際は映像データ取得をクローズ
                if (videoSource.IsRunning)
                {
                    this.CloseVideoSource();
                }
            }
        }

        private void buttonSelectTempImage_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofDialog = new OpenFileDialog();

            // デフォルトのフォルダを指定する
            ofDialog.InitialDirectory = @"C:";

            //ダイアログのタイトルを指定する
            ofDialog.Title = "テンプレート画像を選択";

            //ダイアログを表示する
            if (ofDialog.ShowDialog() == DialogResult.OK)
            {
                Console.WriteLine(ofDialog.FileName);

                buttonSelectTempImage.Text = ofDialog.FileName;

                mat = Cv2.ImRead(ofDialog.FileName);//比較元画像

                //特徴量の検出と特徴量ベクトルの計算
                akaze.DetectAndCompute(mat, null, out key_point1, descriptor1);

                //画像１の特徴点をoutput1に出力
                Cv2.DrawKeypoints(mat, key_point1, output1);
                //Cv2.ImShow("output1", output1);

                pictureBoxTempImage.Image = BitmapConverter.ToBitmap(output1);
            }
            else
            {
                Console.WriteLine("キャンセルされました");
            }

            // オブジェクトを破棄する
            ofDialog.Dispose();
        }
    }
}
