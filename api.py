
from app import generate_frames
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot')
def snapshot():
    return "Snapshot taken (backend not implemented yet)"

@app.route('/report')
def report():
    return "Report generated (backend not implemented yet)"


if __name__ == "__main__":
    app.run(debug=True)
