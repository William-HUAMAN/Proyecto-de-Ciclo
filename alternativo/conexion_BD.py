from pymongo import MongoClient

class Conexion_BD():
    def get_db(self):
        try:
            self.client=MongoClient("mongodb+srv://WilliamHuaman:MUfbSr5qOCkXJWur@proyectoprogramacion.u4hsj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            self.db=self.client.ProyectoProgramacion
        except ConnectionError:
            print('Error de conexion')
        return self.db

    def inicio_sesion(self,email,password):
        pass
    def verificar_mi_conexion(self,codigo_acceso):
        db=self.get_db()
        los_medicos=db.medicos.find({"colegiatura":codigo_acceso},{'_id':1,"nombres":1})#
        for medico in los_medicos:
            print(medico)
        
        