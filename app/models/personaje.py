import datetime


class Personaje:

    def __init__(self, id,name, status, species, name_location, image,url_episodio):
         self.id = id
         self.name=name
         self.status=status
         self.species=species
         self.name_location=name_location
         self.image=image
         self.url_episodio=url_episodio


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'name_location': self.name_location,
            'image': self.image,
            'url_episodio':self.url_episodio
        }