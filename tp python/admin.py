
from PyQt5 import QtCore, QtGui, QtWidgets
from views import adminmainwind , adminask_for_vacation,adminnew ,adminnew_admin ,adminNewTypeOfVacation ,adminsee,adminnew_service,adminaddemploye
from filter import user_session
from connexion import error




class AdminActions(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AdminActions,self).__init__()
        self.ui = adminnew.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.addemployer.clicked.connect(self.add_employe)
        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        # self.ui.delete_2.clicked.connect(self.reset)

        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    # def reset(self):
    #     self.ui.nom.setText("")
    #     self.ui.postnom.setText("")
    #     self.ui.prenom.setText("")
    #     self.ui.adresse.setText("")
    #     self.ui.email.setText("")
    #     self.ui.numerotel.setText("")
    #     self.ui.grade.setText("")

    # def add_employe(self):
    #     if self.verify() : 
    #         pass

    # def verify(self):
    #     message = ""
    #     ret = False
    #     self.ui.nom
    #     if self.ui.postnom & self.ui.prenom & self.ui.adresse & self.ui.email & self.ui.numerotel & self.ui.grade : 
    #         message = " un de champ est vide"
    #         ret = False


    
    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()






class Main(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(Main,self).__init__()
        self.ui = adminmainwind.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        self.ui.nombre_de_demmandes.setText(self.user.nombre_demande)
        self.ui.nombre_de_present.setText(self.user.nombre_present)
        self.ui.nombre_des_absents.setText(self.user.nombre_absent)
        self.ui.nombre_de_demmandes.setText(self.user.nombre_demande)
        self.ui.nombre_de_present.setText(self.user.nombre_present)
        self.ui.nombre_des_absents.setText(self.user.nombre_absent)
        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()











class AddEmploye(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AddEmploye,self).__init__()
        self.ui = adminaddemploye.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()






class NewType(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AddEmploye,self).__init__()
        self.ui = adminaddemploye.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()








class addservice(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(addservice,self).__init__()
        self.ui = adminnew_service.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()










class AddAdmin(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(AddAdmin,self).__init__()
        self.ui = adminnew_admin.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)
        self.ui.comboBox.addItems([""] + self.user.notadmin)

        self.ui.addemployer.clicked.connect(self.ok)
        self.ui.delete_2.clicked.connect(self.remove)

    def ok(self):
        self.selected_empl = self.ui.comboBox.currentText()
        if self.selected_empl.strip() == "":
            self.er = error("veillez selectionner un employer")
            self.er.show()
        else : 
            if self.user.is_admin(self.selected_empl):
                self.er = error(f"{self.selected_empl} est deja un admin " )
                self.er.show()
            else :
                self.er = error(f"{self.selected_empl} est desormais admin " ,False)
                self.user.makeadmin(self.selected_empl)
                self.er.show()

    def remove(self):
        self.selected_empl = self.ui.comboBox.currentText()
        if self.selected_empl.strip() == "":
            self.er = error("veillez selectionner un employer")
            self.er.show()
        else : 
            if not self.user.is_admin(self.selected_empl):
                self.er = error(f"{self.selected_empl} n'est deja pas un  admin")
                self.user.remove_admin(self.selected_empl)
                self.er.show()
            else :
                self.er = error(f"{self.selected_empl} n'est plus admin" ,False)
                self.er.show()




    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()










class Adde(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(Adde,self).__init__()
        self.ui = adminaddemploye.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()










class see(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(see,self).__init__()
        self.ui = adminsee.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ch_data  = []
        self.ch_fields = []

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)

        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

        self.ui.bt_absents.clicked.connect(self.all_absents)
        self.ui.bt_pressents.clicked.connect(self.all_presents)
        self.ui.bt_allusers.clicked.connect(self.all_users)
        self.ui.bt_allasks.clicked.connect(self.all_ask)
        self.ui.bt_all_cvacations.clicked.connect(self.all_vacations)
        self.textchearched = self.ui.lineEdit.text()
        self.all_users()
        self.ui.lineEdit.textEdited.connect(self.on_text_edited)



    def on_text_edited(self):
        fields ,data = self.ui.get_table_data()
        tex_ch = self.ui.lineEdit.text()
        _data  = []
        if tex_ch.strip() == "":
            self.ui.print_data(fields ,data)
        else :
                
            for i in data :
                s = False
                for j in i:
                    if tex_ch in i :
                        s = True
                if s :
                    _data.append(i)
            
            self.ui.print_data(fields , _data)


        print(fields )
        print(data)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()


    def desable(self):

        buttons = [
            self.ui.bt_absents,
            self.ui.bt_all_cvacations,
            self.ui.bt_pressents,
            self.ui.bt_allasks,
            self.ui.bt_allusers,
        ]
        for b in buttons :
            b.setStyleSheet(
                "QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}"
            )

    def active(self ,button :QtWidgets.QPushButton):

          button.setStyleSheet(
                "QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(0,143,150);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(0,0,0,0);\n"

"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(0,143,150);\n"

"}")

    def all_users(self):
        self.desable()
        self.active(self.ui.bt_allusers)
        self.ui.print_data(['username' , 'nom' , 'mail' ,'role' , 'date_creation'],self.user.all_users)

    def all_absents(self):
        self.desable()
        self.active(self.ui.bt_absents)
        self.ui.print_data(['nom', 'prenom', 'date_debut', 'date_fin', 'type_conge'],self.user.all_absent)

    def all_presents(self):
        self.desable()
        self.active(self.ui.bt_pressents)
        self.ui.print_data(['nom', 'prenom'],self.user.all_present)

    def all_vacations(self):
        self.desable()
        self.active(self.ui.bt_all_cvacations)
        self.ui.print_data(['nom' , 'type_conge' ,'date_debut', 'date_fin'] ,  self.user.all_vacation)


    def all_ask(self):
        self.desable()
        self.active(self.ui.bt_allasks)
        self.ui.print_data(['demande_id','nom','prenom', 'type_conge', 'date_debut', 'date_fin', 'statut'],self.user.all_vacation_request)









class Dash(QtWidgets.QMainWindow):
    def __init__(self ,username):
        self.user = user_session(username)


        super(Dash,self).__init__()
        self.ui = adminask_for_vacation.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username.setText( self.user.username)
        self.ui.usertype.setText(self.user.statut)
        self.ui.bn_home.clicked.connect(self.home)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_about.clicked.connect(self.about)
        self.ui.bt_new.clicked.connect(self.new)
        self.ui.bn_close.clicked.connect(self.close)

    def home(self):
        self.wind = Main(self.user.username)
        self.wind.show()
        self.close()

    def about(self):
        self.wind = see(self.user.username)
        self.wind.show()
        self.close()


    def dashboard(self):
        self.wind = Dash(self.user.username)
        self.wind.show()
        self.close()

    def new(self):
        self.wind = AdminActions(self.user.username)
        self.wind.show()
        self.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = AddAdmin("kabudon")


    MainWindow.show()
    sys.exit(app.exec_())