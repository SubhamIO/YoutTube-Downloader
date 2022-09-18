from flask import Flask,request
from pytube import YouTube
app = Flask(__name__)
# savepath = "A:\\my_downloads\\"


@app.route('/')
def hello_world():
    return {'messsage':'Hello World'}

@app.route('/download')
def downloader():
    savepath = request.args.get('savepath')
    link = request.args.get('link')
    print(link)
    try:
        yt = YouTube(link).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download(savepath)
    except:
        print("Connection Error")
    print('Video Downloaded')
    return {'Path': savepath}




if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/download?savepath=A:\\my_downloads\\&link=https://www.youtube.com/shorts/Br0jfcTDZ14
