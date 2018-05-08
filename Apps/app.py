from flask import Flask, render_template, request, json
import socket

app = Flask(__name__)

#	buat object JSON pada python
myNotes = { 'myNotes': [ { 'title' : 'My Extraordinary Title', 'body' : 'This is my sample body text.' } ] }


#	buat default route yang akan menampilkan index.html
@app.route("/")
def main():
	return render_template('index.html', hostname=socket.gethostname())


#	buat route /dataProvider yang akan dipanggil oleh JS saat halaman index.html dibuka
@app.route('/dataProvider', methods=['POST'])
def dataProvider():
	if request.method == 'POST' :
		return json.dumps(myNotes)


#	buat route /submit yang digunakan untuk menambahkan data POST ke objek JSON
@app.route('/submit', methods=['POST'])
def submit():

	_title = request.form['inputTitle']
	_body = request.form['inputBody']

	newJSON = [{ 'title': _title.title() , 'body': _body }]
	myNotes['myNotes'] += newJSON

	return json.dumps(myNotes)


#	jalankan service FLASK pada default port 80
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)