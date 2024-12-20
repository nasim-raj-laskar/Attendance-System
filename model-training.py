from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle

embeddingFile='Attendence-System-Face-Recognition/output/embeddings.pickle'
recognizerFile='Attendence-System-Face-Recognition/output/recognizer.pickle'
labelEncFile='Attendence-System-Face-Recognition/output/le.pickle'

print("Loading face embeddings...")
data=pickle.loads(open(embeddingFile,"rb").read())

print("Encoding Labels...")
labelEnc=LabelEncoder()
labels=labelEnc.fit_transform(data["names"])

print("Training model...")
recognizer=SVC(C=1.0,kernel="linear", probability=True)
recognizer.fit(data["embeddings"],labels)

f=open(recognizerFile,"wb")
f.write(pickle.dumps(recognizer))
f.close()

f=open (labelEncFile,"wb")
f.write(pickle.dumps (labelEnc))
f.close()