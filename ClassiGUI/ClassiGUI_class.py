import tkinter
from time import sleep	

class ClassiGUI_class:

  window = []
  classihubobjectstringvar = []
  rawdatastatusstringvar = []
  loadstopwordstatusstringvar = []
  tokenizestatusstringvar = []
  normalizestatusstringvar = []
  filterstopwordsstatusstringvar = []
  punctuationstatusstringvar = []
  mergenumericstatusstringvar = []
  postagstatusstringvar = []
  lemmatizestatusstringvar = []
  finalizestatusstringvar = []
  tfidfstatusstringvar = []
  transformstatusstringvar = []
  gensimstatusstringvar = []
  glovestatusstringvar = []
  glovegenstatusstringvar = []
  randomforeststatusstringvar = []
  svmlinstatusstringvar = []
  svmpolystatusstringvar = []
  svmrbfstatusstringvar = []
  svmsigmstatusstringvar = []
  decisiontreestatusstringvar = []
  knnstatusstringvar = []
  bayesstatusstringvar = []
  ldastatusstringvar = []
  progressstringvar = []
  tasktitlestringvar = []
  percentagestringvar = []
  randomforestaccstringvar = []
  svmlinaccstringvar = []
  svmpolyaccstringvar = []
  svmrbfaccstringvar = []
  svmsigmoidaccstringvar = []
  dectreeaccstringvar = []
  knnaccstringvar = []
  bayesaccstringvar = []
  ldaaccstringvar = []
  classihubobject = []
  rawdatastatus = []
  loadstopwordstatus = []
  tokenizestatus = []
  normalizestatus = []
  filterstopwordsstatus = []
  punctuationstatus = []
  mergenumericstatus = []
  postagstatus = []
  lemmatizestatus = []
  finalizestatus = []
  tfidfstatus = []
  transformstatus = []
  gensimstatus = []
  glovestatus = []
  glovegenstatus = []
  randomforeststatus = []
  svmlinstatus = []
  svmpolystatus = []
  svmrbfstatus = []
  svmsigmstatus = []
  decisiontreestatus = []
  knnstatus = []
  bayesstatus = []
  randomforestacc = []
  svmlinacc = []
  svmpolyacc = []
  svmrbfacc = []
  svmsigmoidacc = []
  dectreeacc = []
  knnacc = []
  bayesacc = []
  ldaacc = []
  ldastatus = []
  tasktitle = []
  percentage = []
  progress = []
  startbutton = []

  def __init__(self, classihubobject):
    self.classihubobject = classihubobject

  def __process__(self):
    self.window = tkinter.Tk()
    self.classihubobjectstringvar = tkinter.StringVar(self.window)
    self.rawdatastatusstringvar = tkinter.StringVar(self.window)
    self.loadstopwordstatusstringvar = tkinter.StringVar(self.window)
    self.tokenizestatusstringvar = tkinter.StringVar(self.window)
    self.normalizestatusstringvar = tkinter.StringVar(self.window)
    self.filterstopwordsstatusstringvar = tkinter.StringVar(self.window)
    self.punctuationstatusstringvar = tkinter.StringVar(self.window)
    self.mergenumericstatusstringvar = tkinter.StringVar(self.window)
    self.postagstatusstringvar = tkinter.StringVar(self.window)
    self.lemmatizestatusstringvar = tkinter.StringVar(self.window)
    self.finalizestatusstringvar = tkinter.StringVar(self.window)
    self.progressstringvar = tkinter.StringVar(self.window)
    self.tfidfstatusstringvar = tkinter.StringVar(self.window)
    self.transformstatusstringvar = tkinter.StringVar(self.window)
    self.gensimstatusstringvar = tkinter.StringVar(self.window)
    self.glovestatusstringvar = tkinter.StringVar(self.window)
    self.glovegenstatusstringvar = tkinter.StringVar(self.window)
    self.randomforeststatusstringvar = tkinter.StringVar(self.window)
    self.svmlinstatusstringvar = tkinter.StringVar(self.window)
    self.svmpolystatusstringvar = tkinter.StringVar(self.window)
    self.svmrbfstatusstringvar = tkinter.StringVar(self.window)
    self.svmsigmstatusstringvar = tkinter.StringVar(self.window)
    self.decisiontreestatusstringvar = tkinter.StringVar(self.window)
    self.knnstatusstringvar = tkinter.StringVar(self.window)
    self.bayesstatusstringvar = tkinter.StringVar(self.window)
    self.ldastatusstringvar = tkinter.StringVar(self.window)
    self.tasktitlestringvar = tkinter.StringVar(self.window)
    self.percentagestringvar = tkinter.StringVar(self.window)
    self.randomforestaccstringvar = tkinter.StringVar(self.window)
    self.svmlinaccstringvar = tkinter.StringVar(self.window)
    self.svmpolyaccstringvar = tkinter.StringVar(self.window)
    self.svmrbfaccstringvar = tkinter.StringVar(self.window)
    self.svmsigmoidaccstringvar = tkinter.StringVar(self.window)
    self.dectreeaccstringvar = tkinter.StringVar(self.window)
    self.knnaccstringvar = tkinter.StringVar(self.window)
    self.bayesaccstringvar = tkinter.StringVar(self.window)
    self.ldaaccstringvar = tkinter.StringVar(self.window)
    self.window.geometry("850x675")
    self.window.title("Classihub")
    topline = tkinter.Frame(self.window, width = 850, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0).place(x=0, y=00)
    left_border = tkinter.Frame(self.window, width = 50, height = 500, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0).place(x=0, y=50)
    leftpane = tkinter.Frame(self.window, width = 450, height = 500, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1).place(x=50, y = 50)
    middle_border = tkinter.Frame(self.window, width = 50, height = 500, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0).place(x=500, y=50)
    rightpane = tkinter.Frame(self.window, width = 249, height = 500, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1).place(x=550, y=50)
    right_border = tkinter.Frame(self.window, width = 51, height = 500, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0).place(x=799, y=50)
    buttonline = tkinter.Frame(self.window, width = 200, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0).place(x=325, y=550)
    progressline = tkinter.Frame(self.window, width = 750, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1).place(x=50, y=600)
    bottom_border = tkinter.Frame(self.window, width = 850, height = 25, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 0).place(x=0, y=650)
    preprocessor_pane = tkinter.Frame(self.window, width = 140, height = 470, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1).place(x=65, y=65)
    encoder_pane = tkinter.Frame(self.window, width = 140, height = 470, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1).place(x=205, y=65)
    classifier_pane = tkinter.Frame(self.window, width = 140, height = 470, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1).place(x=345, y=65)
    preprocessorlabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "PREPROCESSOR", font=('Helvetica', 8, 'bold')).place(x=70, y=73)
    rawdatalabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Reading raw data").place(x=70, y=96)
    self.rawdatastatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.rawdatastatusstringvar.get())
    self.rawdatastatus.place(x=70, y=118)
    loadstopwordlabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Loading stopwords").place(x=70, y=140)
    self.loadstopwordstatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.loadstopwordstatusstringvar.get())
    self.loadstopwordstatus.place(x=70, y=162)
    tokenizelabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Tokenizing").place(x=70, y=184)
    self.tokenizestatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.tokenizestatusstringvar.get())
    self.tokenizestatus.place(x=70, y=206)
    normalizelabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Normalizing labels").place(x=70, y=228)
    self.normalizestatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.normalizestatusstringvar.get())
    self.normalizestatus.place(x=70, y=250)
    filterstopwordslabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Filtering stopwords").place(x=70, y=272)
    self.filterstopwordsstatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.filterstopwordsstatusstringvar.get())
    self.filterstopwordsstatus.place(x=70, y=294)
    punctuationlabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Filtering punctuation").place(x=70, y=316)
    self.punctuationstatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.punctuationstatusstringvar.get())
    self.punctuationstatus.place(x=70, y=338)
    mergenumericlabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Merging num. tokens").place(x=70, y=360)
    self.mergenumericstatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.mergenumericstatusstringvar.get())
    self.mergenumericstatus.place(x=70, y=382)
    postaglabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "PoS-tagging").place(x=70, y=404)
    self.postagstatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.postagstatusstringvar.get())
    self.postagstatus.place(x=70, y=426)
    lemmatizelabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Lemmatizing").place(x=70, y=448)
    self.lemmatizestatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.lemmatizestatusstringvar.get())
    self.lemmatizestatus.place(x=70, y=470)
    finalizelabel = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Finalizing").place(x=70, y=492)
    self.finalizestatus = tkinter.Label(preprocessor_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.finalizestatusstringvar.get())
    self.finalizestatus.place(x=70, y=514)
    encoderlabel = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "ENCODER", font=('Helvetica', 8, 'bold')).place(x=210, y=73)
    tfidflabel = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "TF-IDF vectorizing").place(x=210, y=96)
    self.tfidfstatus = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.tfidfstatusstringvar.get())
    self.tfidfstatus.place(x=210, y=118)
    transformlabel = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Transforming data").place(x=210, y=140)
    self.transformstatus = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.transformstatusstringvar.get())
    self.transformstatus.place(x=210, y=162)
    gensimlabel = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Loading Gensim model").place(x=210, y=184)
    self.gensimstatus = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.gensimstatusstringvar.get())
    self.gensimstatus.place(x=210, y=206)
    glovelabel = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Loading GloVe data").place(x=210, y=228)
    self.glovestatus = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.glovestatusstringvar.get())
    self.glovestatus.place(x=210, y=250)
    glovegenlabel = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Generating GloVe model").place(x=210, y=272)
    self.glovegenstatus = tkinter.Label(encoder_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.glovegenstatusstringvar.get())
    self.glovegenstatus.place(x=210, y=294)
    classifierlabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "CLASSIFIER", font=('Helvetica', 8, 'bold')).place(x=350, y=73)
    randomforestlabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Random Forest").place(x=350, y=96)
    self.randomforeststatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.randomforeststatusstringvar.get())
    self.randomforeststatus.place(x=350, y=118)
    svmlinlabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "SVM Linear").place(x=350, y=140)
    self.svmlinstatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.svmlinstatusstringvar.get())
    self.svmlinstatus.place(x=350, y=162)
    svmpolylabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "SVM Polynomial").place(x=350, y=184)
    self.svmpolystatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.svmpolystatusstringvar.get())
    self.svmpolystatus.place(x=350, y=206)
    svmrbflabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "SVM RBF").place(x=350, y=228)
    self.svmrbfstatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.svmrbfstatusstringvar.get())
    self.svmrbfstatus.place(x=350, y=250)
    svmsigmlabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "SVM Sigmoid").place(x=350, y=272)
    self.svmsigmstatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.svmsigmstatusstringvar.get())
    self.svmsigmstatus.place(x=350, y=294)
    decisiontreelabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Decision Tree").place(x=350, y=316)
    self.decisiontreestatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.decisiontreestatusstringvar.get())
    self.decisiontreestatus.place(x=350, y=338)
    knnlabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "K-Nearest Neighbors").place(x=350, y=360)
    self.knnstatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.knnstatusstringvar.get())
    self.knnstatus.place(x=350, y=382)
    bayeslabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "Naive Bayes").place(x=350, y=404)
    self.bayesstatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.bayesstatusstringvar.get())
    self.bayesstatus.place(x=350, y=426)
    ldalabel = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = "LDA").place(x=350, y=448)
    self.ldastatus = tkinter.Label(classifier_pane, width = 18, height = 1, borderwidth=1, relief="solid", text = self.ldastatusstringvar.get())
    self.ldastatus.place(x=350, y=470)
    accuracylabel = tkinter.Label(classifier_pane, width = 35, height = 1, borderwidth=1, relief="solid", text = "ACCURACY METRICS", font=('Helvetica', 8, 'bold')).place(x=550.45, y=50)
    randomforestacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "Random Forest").place(x=565, y=73)
    self.randomforestacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.randomforestaccstringvar.get())
    self.randomforestacc.place(x=565, y=95)
    svmlinacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "SVM Linear").place(x=565, y=117)
    self.svmlinacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.svmlinaccstringvar.get())
    self.svmlinacc.place(x=565, y=139)
    svmpolyacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "SVM Polynomial").place(x=565, y=161)
    self.svmpolyacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.svmpolyaccstringvar.get())
    self.svmpolyacc.place(x=565, y=183)
    svmrbfacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "SVM RBF").place(x=565, y=205)
    self.svmrbfacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.svmrbfaccstringvar.get())
    self.svmrbfacc.place(x=565, y=227)
    svmsigmoidacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "SVM Sigmoid").place(x=565, y=249)
    self.svmsigmoidacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.svmsigmoidaccstringvar.get())
    self.svmsigmoidacc.place(x=565, y=271)
    dectreeacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "Decision Tree").place(x=565, y=293)
    self.dectreeacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.dectreeaccstringvar.get())
    self.dectreeacc.place(x=565, y=315)
    knnacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "K-Nearest Neighbors").place(x=565, y=337)
    self.knnacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.knnaccstringvar.get())
    self.knnacc.place(x=565, y=359)
    bayesacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "Naive Bayes").place(x=565, y=381)
    self.bayesacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.bayesaccstringvar.get())
    self.bayesacc.place(x=565, y=403)
    ldaacclabel = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = "LDA").place(x=565, y=425)
    self.ldaacc = tkinter.Label(rightpane, width = 30, height = 1, borderwidth=1, relief="solid", text = self.ldaaccstringvar.get())
    self.ldaacc.place(x=565, y=447)
    self.startbutton = tkinter.Button(self.window,text="Start evaluation", command=self.__Start_Process__)
    self.startbutton.place(x=370,y=560)
    self.progress = tkinter.Label(rightpane, width = 102, height = 2, borderwidth=1, relief="solid", anchor="w", text = self.progressstringvar.get())
    self.progress.place(x=65, y=607)
    self.tasktitle = tkinter.Label(rightpane, width = 30, height = 2, borderwidth=1, relief="solid", anchor="w", text = self.tasktitlestringvar.get())
    self.tasktitle.place(x=65, y=560)
    self.percentage = tkinter.Label(rightpane, width = 20, height = 2, borderwidth=1, relief="solid", anchor="e", text = self.percentagestringvar.get())
    self.percentage.place(x=640, y=560)
    print("Type is " + str(type(self.progress)))
    print("Type is " + str(type(self.percentage)))
    print("Type is " + str(type(self.tasktitle)))

    self.classihubobjectstringvar.set("---")
    self.rawdatastatusstringvar.set("---")
    self.loadstopwordstatusstringvar.set("---")
    self.tokenizestatusstringvar.set("---")
    self.normalizestatusstringvar.set("---")
    self.filterstopwordsstatusstringvar.set("---")
    self.punctuationstatusstringvar.set("---")
    self.mergenumericstatusstringvar.set("---")
    self.postagstatusstringvar.set("---")
    self.lemmatizestatusstringvar.set("---")
    self.finalizestatusstringvar.set("---")
    self.tfidfstatusstringvar.set("---")
    self.transformstatusstringvar.set("---")
    self.gensimstatusstringvar.set("---")
    self.glovestatusstringvar.set("---")
    self.glovegenstatusstringvar.set("---")
    self.randomforeststatusstringvar.set("---")
    self.svmlinstatusstringvar.set("---")
    self.svmpolystatusstringvar.set("---")
    self.svmrbfstatusstringvar.set("---")
    self.svmsigmstatusstringvar.set("---")
    self.decisiontreestatusstringvar.set("---")
    self.knnstatusstringvar.set("---")
    self.bayesstatusstringvar.set("---")
    self.ldastatusstringvar.set("---")
    self.randomforestaccstringvar.set("---")
    self.svmlinaccstringvar.set("---")
    self.svmpolyaccstringvar.set("---")
    self.svmrbfaccstringvar.set("---")
    self.svmsigmoidaccstringvar.set("---")
    self.dectreeaccstringvar.set("---")
    self.knnaccstringvar.set("---")
    self.bayesaccstringvar.set("---")
    self.ldaaccstringvar.set("---")
    self.progressstringvar.set("----------------------------------------------------")
    self.window.mainloop()
	
  def __Start_Process__(self):
    self.startbutton.config(state = "disabled")
    sleep(0.001)
    self.window.update()
    self.classihubobject.__process__()
    