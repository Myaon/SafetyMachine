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

using Original;

namespace PcCameraApp
{
    partial class MainForm
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.comboBoxCameraType = new System.Windows.Forms.ComboBox();
            this.buttonStartStop = new System.Windows.Forms.Button();
            this.labelFps = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.pictureBoxCamera = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.pictureBoxTempImage = new System.Windows.Forms.PictureBox();
            this.buttonSelectTempImage = new System.Windows.Forms.Button();
            this.labelResult = new System.Windows.Forms.Label();
            this.pictureBoxResult = new System.Windows.Forms.PictureBox();
            this.labelMatch = new System.Windows.Forms.Label();
            this.checkBoxAlert = new System.Windows.Forms.CheckBox();
            this.checkBoxStop = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxCamera)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxTempImage)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxResult)).BeginInit();
            this.SuspendLayout();
            // 
            // comboBoxCameraType
            // 
            this.comboBoxCameraType.FormattingEnabled = true;
            this.comboBoxCameraType.Location = new System.Drawing.Point(218, 27);
            this.comboBoxCameraType.Name = "comboBoxCameraType";
            this.comboBoxCameraType.Size = new System.Drawing.Size(317, 25);
            this.comboBoxCameraType.TabIndex = 0;
            // 
            // buttonStartStop
            // 
            this.buttonStartStop.Font = new System.Drawing.Font("メイリオ", 8.142858F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.buttonStartStop.Location = new System.Drawing.Point(736, 23);
            this.buttonStartStop.Name = "buttonStartStop";
            this.buttonStartStop.Size = new System.Drawing.Size(102, 45);
            this.buttonStartStop.TabIndex = 1;
            this.buttonStartStop.Text = "開始";
            this.buttonStartStop.UseVisualStyleBackColor = true;
            this.buttonStartStop.Click += new System.EventHandler(this.button1_Click);
            // 
            // labelFps
            // 
            this.labelFps.Font = new System.Drawing.Font("メイリオ", 8.142858F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelFps.Location = new System.Drawing.Point(736, 82);
            this.labelFps.Name = "labelFps";
            this.labelFps.Size = new System.Drawing.Size(102, 36);
            this.labelFps.TabIndex = 4;
            this.labelFps.Text = "FPS";
            this.labelFps.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // pictureBoxCamera
            // 
            this.pictureBoxCamera.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxCamera.Location = new System.Drawing.Point(34, 142);
            this.pictureBoxCamera.Name = "pictureBoxCamera";
            this.pictureBoxCamera.Size = new System.Drawing.Size(640, 420);
            this.pictureBoxCamera.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBoxCamera.TabIndex = 5;
            this.pictureBoxCamera.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(39, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(96, 17);
            this.label1.TabIndex = 6;
            this.label1.Text = "カメラデバイス：";
            // 
            // pictureBoxTempImage
            // 
            this.pictureBoxTempImage.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxTempImage.Location = new System.Drawing.Point(697, 142);
            this.pictureBoxTempImage.Name = "pictureBoxTempImage";
            this.pictureBoxTempImage.Size = new System.Drawing.Size(640, 420);
            this.pictureBoxTempImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBoxTempImage.TabIndex = 9;
            this.pictureBoxTempImage.TabStop = false;
            // 
            // buttonSelectTempImage
            // 
            this.buttonSelectTempImage.Font = new System.Drawing.Font("メイリオ", 8.142858F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(128)));
            this.buttonSelectTempImage.Location = new System.Drawing.Point(34, 70);
            this.buttonSelectTempImage.Name = "buttonSelectTempImage";
            this.buttonSelectTempImage.Size = new System.Drawing.Size(501, 49);
            this.buttonSelectTempImage.TabIndex = 10;
            this.buttonSelectTempImage.Text = "テンプレート画像を開く";
            this.buttonSelectTempImage.UseVisualStyleBackColor = true;
            this.buttonSelectTempImage.Click += new System.EventHandler(this.buttonSelectTempImage_Click);
            // 
            // labelResult
            // 
            this.labelResult.Font = new System.Drawing.Font("メイリオ", 8.142858F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelResult.Location = new System.Drawing.Point(869, 27);
            this.labelResult.Name = "labelResult";
            this.labelResult.Size = new System.Drawing.Size(102, 36);
            this.labelResult.TabIndex = 11;
            this.labelResult.Text = "判定結果";
            this.labelResult.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // pictureBoxResult
            // 
            this.pictureBoxResult.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxResult.Location = new System.Drawing.Point(46, 142);
            this.pictureBoxResult.Name = "pictureBoxResult";
            this.pictureBoxResult.Size = new System.Drawing.Size(1280, 420);
            this.pictureBoxResult.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBoxResult.TabIndex = 12;
            this.pictureBoxResult.TabStop = false;
            // 
            // labelMatch
            // 
            this.labelMatch.Font = new System.Drawing.Font("メイリオ", 8.142858F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelMatch.Location = new System.Drawing.Point(869, 82);
            this.labelMatch.Name = "labelMatch";
            this.labelMatch.Size = new System.Drawing.Size(102, 36);
            this.labelMatch.TabIndex = 13;
            this.labelMatch.Text = "類似特徴点数";
            this.labelMatch.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // checkBoxAlert
            // 
            this.checkBoxAlert.AutoSize = true;
            this.checkBoxAlert.Font = new System.Drawing.Font("メイリオ", 10F);
            this.checkBoxAlert.Location = new System.Drawing.Point(581, 34);
            this.checkBoxAlert.Name = "checkBoxAlert";
            this.checkBoxAlert.Size = new System.Drawing.Size(113, 25);
            this.checkBoxAlert.TabIndex = 14;
            this.checkBoxAlert.Text = "アラート機能";
            this.checkBoxAlert.UseVisualStyleBackColor = true;
            // 
            // checkBoxStop
            // 
            this.checkBoxStop.AutoSize = true;
            this.checkBoxStop.Font = new System.Drawing.Font("メイリオ", 10F);
            this.checkBoxStop.Location = new System.Drawing.Point(581, 83);
            this.checkBoxStop.Name = "checkBoxStop";
            this.checkBoxStop.Size = new System.Drawing.Size(113, 25);
            this.checkBoxStop.TabIndex = 14;
            this.checkBoxStop.Text = "非常停止機能";
            this.checkBoxStop.UseVisualStyleBackColor = true;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 17F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1371, 584);
            this.Controls.Add(this.checkBoxStop);
            this.Controls.Add(this.checkBoxAlert);
            this.Controls.Add(this.labelMatch);
            this.Controls.Add(this.pictureBoxResult);
            this.Controls.Add(this.labelResult);
            this.Controls.Add(this.buttonSelectTempImage);
            this.Controls.Add(this.pictureBoxTempImage);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pictureBoxCamera);
            this.Controls.Add(this.labelFps);
            this.Controls.Add(this.buttonStartStop);
            this.Controls.Add(this.comboBoxCameraType);
            this.Font = new System.Drawing.Font("メイリオ", 8.142858F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Name = "MainForm";
            this.Text = "PCカメラ映像取得ソフト";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxCamera)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxTempImage)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxResult)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox comboBoxCameraType;
        private System.Windows.Forms.Button buttonStartStop;
        private System.Windows.Forms.Label labelFps;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.PictureBox pictureBoxCamera;
        private System.Windows.Forms.Label label1;
        private PictureBox pictureBoxTempImage;
        private Button buttonSelectTempImage;
        private PictureBox pictureBoxResult;
        public Label labelResult;
        public Label labelMatch;
        private CheckBox checkBoxAlert;
        private CheckBox checkBoxStop;
    }
}

