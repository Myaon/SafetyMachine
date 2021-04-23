using OpenCvSharp;
using OpenCvSharp.Extensions;
using System;
using System.Drawing;

/// <summary>
/// オリジナルクラス
/// </summary>
namespace Original
{
    public class OpenCVSharpBitmap : IDisposable
    {
        private Mat mat;

        /// <summary>
        /// コンストラクタ
        /// </summary>
        /// <param name="img"></param>
        public OpenCVSharpBitmap(Bitmap img)
        {
            this.mat = BitmapConverter.ToMat(img);
        }

        public void Dispose()
        {
            ((IDisposable)mat).Dispose();
        }

        /// <summary>
        /// グレーに変換したBitmapを取得
        /// </summary>
        /// <returns></returns>
        public Bitmap toGray()
        {
            Mat matGray = mat.CvtColor(ColorConversionCodes.BGR2GRAY);
            return BitmapConverter.ToBitmap(matGray);
        }

        /// <summary>
        /// 顔を認識して赤枠を追加したBitmapを取得
        /// </summary>
        /// <param name="cascadePath"></param>
        /// <returns></returns>
        public Bitmap addFaceRect(string @cascadePath)
        {
            // 分類機の用意
            using (CascadeClassifier cascade = new CascadeClassifier(@cascadePath))
            {
                foreach (Rect rectFace in cascade.DetectMultiScale(mat))
                {
                    // 見つかった場所に赤枠を表示
                    Rect rect = new Rect(rectFace.X, rectFace.Y, rectFace.Width, rectFace.Height);
                    mat.Rectangle(rect, new OpenCvSharp.Scalar(0,0,255), 3, LineTypes.Link8);
                }
            }

            return BitmapConverter.ToBitmap(mat);
        }
    }
}