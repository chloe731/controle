note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)


notes = [note1, note2, note3, note4, note5, note6,note7,note8]

#print(note1[0])


#moyenne1 = (notes[0][2] + notes[1][2] + notes[2][2] + notes[3][2] + notes[4][2] + notes[5][2])/6
#print("Moyenne élèvé 1 : ",moyenne1)


#moyenne1_math = (notes[0][2] + notes[2][2]+ notes[5][2])/3
#print("Moyenne élèvé 1 en mathématiques : ",moyenne1_math)




def moyenne_eleve1(liste):
  moyenne = [ item[2]  for item in liste if  item[0]=="eleve1"]
  moyenne1 = sum(moyenne)/len(moyenne)
  return moyenne1
print(moyenne_eleve1(notes))



def moyenne_eleve1(liste):
  moyenne = [ item[2]  for item in liste if  item[0]=="eleve1" and item[1]=="math" ]
  moyenne1 = sum(moyenne)/len(moyenne)
  return moyenne1
print(moyenne_eleve1(notes))



def moyenne_tuple(notes, eleve, matiere):
  moyenne = [x for x in notes if x[0] == eleve]
  moyenne_matiere = [x for x in moyenne if x[1] == matiere]
  return sum([x[2] for x in moyenne_matiere ])/len(moyenne_matiere )

m = moyenne_tuple(notes,'eleve1','math')
print(m)
  
# Que se passe-t-il si on fait une faute de frappe dans la saisie d'une matière ? 
# Le logiciel ne trouve pas de matière donc ne renvoie rien car il ne peut pas calculer la moyenne

# Que se passe-t-il si quelqu'un rentre une chaine de caractère au lieu d'une nombre '14' au lieu de 14 ?
# Cela renvoie une erreur comme quoi le paramètre n'est pas défini.


# Que se passe-t-il si on veut ajouter des coefficient aux notes et aux matières ? 
# Il faut modifier la fonction car les coefficients ne sont pas pris en compte dans la fonction.

# Que se passe-t-il si on a un triplet qui n'est pas du tout une note ?
# Cela ne fonctionne pas 

class Note:
  instances = []
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    self.instances.append(self)


  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"
  @classmethod
 
 
  def vider(cls):
    cls.instances = []
  
  
  def afficher(self):
      print(self)
 
 
  @classmethod
  def moyenne(cls, eleve=None, matiere=None):
      print('****', cls.instances)
      moyenne = [x for x in cls.instances if x.eleve == eleve] if eleve is not None else _notes
      moyenne_matiere = [x for x in moyenne if x.matiere == matiere] if matiere is not None else moyenne
      return sum([x.valeur for x in moyenne_matiere])/len(moyenne_matiere)


onote = Note('eleve1', 'maths', 13)

print(onote.matiere)

print(onote.valeur)

Note.afficher(onote)



onotes=[Note(x,y,z) for x,y,z in notes]

Note.moyenne('eleve2', 'math')

notes_enregistrées = []



def moyenne_Note(notes, eleve = None, matiere = None):
  moyenne = [x for x in notes if x.eleve == eleve] if eleve is not None else notes
  moyenne_matiere = [x for x in moyenne if x.matiere == matiere] if matiere is not None else moyenne
  return sum([x.valeur for x in moyenne_matiere])/len(moyenne_matiere)
