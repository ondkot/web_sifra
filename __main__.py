from os import system
import flask
app = flask.Flask(__name__)
def ceaserSifruj(text,klic):
	mala = "abcdefghijklmnopqrstuvwxyz"
	velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sifra = text.upper()
	klic = klic.upper()
	if (klic not in mala and klic not in velka) or len(klic) != 1:
		return "Klíč musí být jedno písmeno."
	klic = velka.find(klic)
	vysledek = []
	for i in range(0,len(sifra)):
		pomocna = velka.find(sifra[i])
		pomocna = pomocna + klic
		while pomocna > 25:
			pomocna -= 25
		vysledek.append(velka[pomocna])
	return "Zašifrovaný text je: " + ''.join(vysledek)
def ceaserDesifruj(text,klic):
	mala = "abcdefghijklmnopqrstuvwxyz"
	velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sifra = text.upper()
	if (klic not in mala and klic not in velka) or len(klic) != 1:
		return "Klíč musí být jedno písmeno."
	klic = klic.upper()
	klic = velka.find(klic)
	vysledek = []
	for i in range(0,len(sifra)):
		pomocna = velka.find(sifra[i])
		pomocna -= klic
		while pomocna < 0:
			pomocna += 25
		vysledek.append(velka[pomocna])
	return "Dešifrovaný text je: " + ''.join(vysledek)
@app.route("/")
def index():
	return ""
@app.route("/ceasar")
def ceaser():
	return "Použijte adresu http://127.0.0.1:5000/ceasar/sifruj/?text=text&klic=klic pro zašifrování, adresu http://127.0.0.1:5000/ceasar/desifruj/?text=text&klic=klic pro dešifrování."
@app.route("/ceasar/sifruj")
def sifruj():
	text = flask.request.args.get("text")
	if text == None:
		return "Použijte adresu http://127.0.0.1:5000/ceasar/sifruj/?text=text&klic=klic."
	klic = flask.request.args.get("klic")
	if klic == None:
		return "Použijte adresu http://127.0.0.1:5000/ceasar/sifruj/?text=text&klic=klic."
	return ceaserSifruj(text,klic)
@app.route("/ceaser/desifruj")
def desifruj():
	text = flask.request.args.get("text")
	if text == None:
		return "Použijte adresu http://127.0.0.1:5000/ceasar/desifruj/?text=text&klic=klic."
	klic = flask.request.args.get("klic")
	if klic == None:
		return "Použijte adresu http://127.0.0.1:5000/ceasar/desifruj/?text=text&klic=klic."
	return ceaserDesifruj(text,klic)
app.run(host="0.0.0.0")