from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from app import db
from app.models import Client, Document, Employe
from app.models import Employe

main_bp = Blueprint('main', __name__)

@main_bp.route('/ajouter_employe', methods=['GET', 'POST'])
def ajouter_employe():
    if request.method == 'POST':
        if request.headers.get('Accept') == 'application/json':
            nom = request.form['nom']
            prenom = request.form['prenom']
            email = request.form['email']
            poste = request.form['poste']
            employe = Employe(nom=nom, prenom=prenom, email=email, poste=poste)
            db.session.add(employe)
            db.session.commit()
            return jsonify({
                'success': True,
                'message': 'Employé ajouté avec succès!',
                'redirect_url': url_for('main.employes')
            })
        else:
            nom = request.form['nom']
            prenom = request.form['prenom']
            email = request.form['email']
            poste = request.form['poste']
            employe = Employe(nom=nom, prenom=prenom, email=email, poste=poste)
            db.session.add(employe)
            db.session.commit()
            flash('Employé ajouté avec succès!', 'success')
            return redirect(url_for('main.employes'))
    return render_template('ajouter_employe.html')