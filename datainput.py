from models import *


def add_genres(*args, **kwargs):
    rcrds = Genre.query.all()
    if len(rcrds) == 0:
        g1 = Genre(name='Alternative')
        g2 = Genre(name='Blues')
        g3 = Genre(name='Country')
        g4 = Genre(name='Electronic')
        g5 = Genre(name='Folk')
        g6 = Genre(name='Funk')
        g7 = Genre(name='Hip-Hop')
        g8 = Genre(name='Heavy Metal')
        g9 = Genre(name='Instrumental')
        g10 = Genre(name='Musical Theatre')
        g18 = Genre(name='Classical')
        g11 = Genre(name='Jazz')
        g12 = Genre(name='Pop')
        g13 = Genre(name='Punk')
        g14 = Genre(name='R&B')
        g15 = Genre(name='Rock')
        g16 = Genre(name='Soul')
        g17 = Genre(name='Other')
        g19 = Genre(name='Reggae')

        db.session.add(g1)
        db.session.add(g2)
        db.session.add(g3)
        db.session.add(g4)
        db.session.add(g5)
        db.session.add(g6)
        db.session.add(g7)
        db.session.add(g19)
        db.session.add(g8)
        db.session.add(g9)
        db.session.add(g10)
        db.session.add(g18)
        db.session.add(g11)
        db.session.add(g12)
        db.session.add(g13)
        db.session.add(g14)
        db.session.add(g15)
        db.session.add(g16)
        db.session.add(g17)
        # db.session.add_all(
        #     [Genre(name='Alternative'), Genre(name='Blues'), Genre(name='Country'), Genre(name='Electronic'), Genre(name='Folk'), Genre(name='Funk'), Genre(name='Hip-Hop'), Genre(name='Heavy Metal'), Genre(name='Instrumental'), Genre(name='Jazz'), Genre('Musical Theatre'), Genre(name='Pop'), Genre(nmae='Punk'), Genre(name='R&B'), Genre(name='Rock'), Genre('Soul'), Genre(name='Other')]
        # )

        db.session.flush()
        db.session.refresh(g1, attribute_names=['id'])
        
    return add_cities()

  
def add_cities(*args, **kwargs):
    rcrds = City.query.all()
    if len(rcrds) == 0:
        sf = City(name='San Francisco', state='CA')
        la = City(name='Los Angeles', state='CA')
        ny = City(name='New York', state='NY')
        nola = City(name='New Orleans', state='LA')

        db.session.add(sf)
        db.session.add(la)
        db.session.add(ny)
        db.session.add(nola)

        db.session.commit()
        
    
    return add_venues()

def add_venues(*args, **kwargs):
    print(Genre.query.filter_by(name='Classical').first())
    rcrds = Venue.query.all()
    if len(rcrds) == 0:
        jazz = Genre.query.filter_by(name='Jazz').first()
        classical = Genre.query.filter_by(name='Classical').first()
        rb = Genre.query.filter_by(name='R&B').first()
        hh=  Genre.query.filter_by(name='Hip-Hop').first()
        folk =  Genre.query.filter_by(name='Folk').first()
        blues = Genre.query.filter_by(name='Blues').first()
        funk = Genre.query.filter_by(name='Funk').first()
        rock = Genre.query.filter_by(name='Rock').first()

        sf_id = City.query.filter_by(name='San Francisco').first().id
        ny_id = City.query.filter_by(name='New York').first().id
        
        venue = Venue(name='Park Square Live Music & Coffee', city_id=sf_id, address='123 Seseame St', phone='123-123-1234', image_link='https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80', seeking_talent=False, website='', genres=[jazz, classical] )
        venue2 = Venue(name='The Dueling Pianos Bar', city_id=ny_id, address='335 Delancey Street', phone='914-003-1132', image_link='https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80', facebook_link='https://www.facebook.com/theduelingpiano',  seeking_talent=False, website='https://www.theduelingpianos.com', genres=[classical, rb, hh] )
        venue3 = Venue(name='The Musical Hop', city_id=ny_id, address='1015 Folsom Street', phone='123-123-1234', image_link='https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60', facebook_link='https://www.facebook.com/TheMusicalHop',  seeking_talent=True, seeking_description='We are on the lookout for a local artist to play every two weeks. Please call us.', website='https://www.themusicalhop.com', genres= [rock])
      

        db.session.add(venue)
        db.session.add(venue2)
        db.session.add(venue3)

        db.session.commit()
        
    
    return add_artists()


def add_artists(*args, **kwargs):
    rcrds = Artist.query.all()
    if len(rcrds) == 0:
        sf_id = City.query.filter_by(name='San Francisco').first().id
        ny_id = City.query.filter_by(name='New York').first().id
        nola_id = City.query.filter_by(name='New Orleans').first().id

        jazz = Genre.query.filter_by(name='Jazz').first()
        classical = Genre.query.filter_by(name='Classical').first()
        folk =  Genre.query.filter_by(name='Folk').first()
        punk = Genre.query.filter_by(name='Punk').first()
        rock = Genre.query.filter_by(name='Rock').first()
        reggae = Genre.query.filter_by(name='Reggae').first()

        GNP = Artist(name='Guns N Petals', phone='326-123-5000', city_id=sf_id, website='https://www.gunsnpetalsband.com', image_link='https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=8', facebook_link='https://www.facebook.com/GunsNPetals', seeking_venues=True, seeking_description='Looking for shows to perform at in the San Francisco Bay Area!', genres=[rock])

        MQ = Artist(name='Matt Quevedo', phone='123-123-2222', city_id=ny_id, website='https://www.mattqevedo.com', image_link='https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80', facebook_link='https://www.facebook.com/mattquevedo923251523', seeking_venues=False, genres=[jazz])

        WSB = Artist(name='The Wild Sax Band', phone='432-325-5432', city_id=sf_id, website='https://www.wildsaxons.com', image_link='https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80', seeking_venues=False, genres=[jazz, classical])

        MHR = Artist(name='Miyagi\'s Holly Rollers', phone='504-666-7777', city_id=nola_id, website='https://www.waxon.com', image_link='https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60', seeking_venues=False, genres=[jazz, reggae, folk, punk])

        db.session.add(GNP)
        db.session.add(MQ)
        db.session.add(WSB)
        db.session.add(MHR)

        db.session.commit()
        
    return shows()
   
def shows(*args, **kwargs):
    if not Show.query.all():
        hop_venue = Venue.query.filter_by(name='The Musical Hop').first()
        GnP = Artist.query.filter_by(name='Guns N Petals').first()

        show1 = Show(artist_id = GnP.id, venue_id=hop_venue.id, start_time='2019-05-21T21:30:00.000Z')
        
        v = Venue.query.filter_by(name='Park Square Live Music & Coffee').first()
        a = Artist.query.filter_by(name='Matt Quevedo').first()

        show2 = Show(artist_id = a.id, venue_id=v.id, start_time='2019-06-15T23:00:00.000Z')


        a = Artist.query.filter_by(name='The Wild Sax Band').first()

        show3 = Show(artist_id = a.id, venue_id=v.id, start_time='2035-04-08T20:00:00.000Z')

        show4 = Show(artist_id = a.id, venue_id=v.id, start_time='2035-04-15T20:00:00.000Z')

        db.session.add(show1)
        db.session.add(show2)
        db.session.add(show3)
        db.session.add(show4)

        db.session.commit()
        db.session.close()
    else:
        db.session.close()
    return None

