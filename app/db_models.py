from app import db

class PackDay(db.Model):
    __tablename__ = 'packday'
    id = db.Column(db.Integer, primary_key=True)
    packege = db.Column("Пакет", db.ForeignKey('toursinfo.id'))

    #===1st day===
    first_city = db.Column(db.String(50), nullable=False)
    first = db.Column(db.String(255), nullable=False)
    enfirstcity = db.Column(db.String(50), nullable=False)
    enfirst = db.Column(db.String(255), nullable=False)

    # ===2nd day===
    second_city = db.Column(db.String(50), nullable=False)
    second = db.Column(db.String(255), nullable=False)
    ensecondcity = db.Column(db.String(50), nullable=False)
    ensecond = db.Column(db.String(255), nullable=False)

    # ===3rd day===
    third_city = db.Column(db.String(50), nullable=False)
    third = db.Column(db.String(255), nullable=False)
    enthirdcity = db.Column(db.String(50), nullable=False)
    enthird = db.Column(db.String(255), nullable=False)

    # ===4th day===
    four_city = db.Column(db.String(50), nullable=False)
    four = db.Column(db.String(255), nullable=False)
    enfourcity = db.Column(db.String(50), nullable=False)
    enfour = db.Column(db.String(255), nullable=False)

    # ===5th day===
    five_city = db.Column(db.String(50), nullable=False)
    five = db.Column(db.String(255), nullable=False)
    enfivecity = db.Column(db.String(50), nullable=False)
    enfive = db.Column(db.String(255), nullable=False)

    # ===6th day===
    six_city = db.Column(db.String(50), nullable=False)
    six = db.Column(db.String(255), nullable=False)
    ensixcity = db.Column(db.String(50), nullable=False)
    ensix = db.Column(db.String(255), nullable=False)

    # ===7th day===
    seven_city = db.Column(db.String(50), nullable=False)
    seven = db.Column(db.String(255), nullable=False)
    ensevencity = db.Column(db.String(50), nullable=False)
    enseven = db.Column(db.String(255), nullable=False)

    # ===8th day===
    eight_city = db.Column(db.String(50), nullable=False)
    eight = db.Column(db.String(255), nullable=False)
    eneightcity = db.Column(db.String(50), nullable=False)
    eneight = db.Column(db.String(255), nullable=False)

    # ===9th day===
    nine_city = db.Column(db.String(50), nullable=False)
    nine = db.Column(db.String(255), nullable=False)
    enninecity = db.Column(db.String(50), nullable=False)
    ennine = db.Column(db.String(255), nullable=False)

   # ===10th day===
    ten_city = db.Column(db.String(50), nullable=False)
    ten = db.Column(db.String(255), nullable=False)
    entencity = db.Column(db.String(50), nullable=False)
    enten = db.Column(db.String(255), nullable=False)

    # ===11th day===
    eleven_city = db.Column(db.String(50), nullable=False)
    eleven = db.Column(db.String(255), nullable=False)
    enelevencity = db.Column(db.String(50), nullable=False)
    eneleven = db.Column(db.String(255), nullable=False)

    # ===12th day===
    twelve_city = db.Column(db.String(50), nullable=False)
    twelve = db.Column(db.String(255), nullable=False)
    entwelvecity = db.Column(db.String(50), nullable=False)
    entwelve = db.Column(db.String(255), nullable=False)

    # ===13th day===
    thirdteen_city = db.Column(db.String(50), nullable=False)
    thirdteen = db.Column(db.String(255), nullable=False)
    enthirdteencity = db.Column(db.String(50), nullable=False)
    enthirdteen = db.Column(db.String(255), nullable=False)

    # ===14th day===
    fourteen_city = db.Column(db.String(50), nullable=False)
    fourteen = db.Column(db.String(255), nullable=False)
    enfourteencity = db.Column(db.String(50), nullable=False)
    enfourteen = db.Column(db.String(255), nullable=False)

    # ===15th day===
    fiveteen_city = db.Column(db.String(50), nullable=False)
    fiveteen = db.Column(db.String(255), nullable=False)
    enfiveteencity = db.Column(db.String(50), nullable=False)
    enfiveteen = db.Column(db.String(255), nullable=False)

    # ===16th day===
    sixteen_city = db.Column(db.String(50), nullable=False)
    sixteen = db.Column(db.String(255), nullable=False)
    ensixteencity = db.Column(db.String(50), nullable=False)
    ensixteen = db.Column(db.String(255), nullable=False)

    # ===17th day===
    seventeen_city = db.Column(db.String(50), nullable=False)
    seventeen = db.Column(db.String(255), nullable=False)
    enseventeencity = db.Column(db.String(50), nullable=False)
    enfirst = db.Column(db.String(255), nullable=False)

    # ===18th day===
    eightteen_city = db.Column(db.String(50), nullable=False)
    eightteen = db.Column(db.String(255), nullable=False)
    eneightteencity = db.Column(db.String(50), nullable=False)
    eneightteen = db.Column(db.String(255), nullable=False)

    # ===19th day===
    nineteen_city = db.Column(db.String(50), nullable=False)
    nineteen = db.Column(db.String(255), nullable=False)
    ennineteencity = db.Column(db.String(50), nullable=False)
    ennineteen = db.Column(db.String(255), nullable=False)

    # ===20th day===
    twelve_city = db.Column(db.String(50), nullable=False)
    twelve = db.Column(db.String(255), nullable=False)
    entwelvecity = db.Column(db.String(50), nullable=False)
    entwelve = db.Column(db.String(255), nullable=False)

    # ===21th day===
    twentyone_city = db.Column(db.String(50), nullable=False)
    twentyone = db.Column(db.String(255), nullable=False)
    entwentyonecity = db.Column(db.String(50), nullable=False)
    entwentyone = db.Column(db.String(255), nullable=False)

    # ===22th day===
    twentytwo_city = db.Column(db.String(50), nullable=False)
    twentytwo = db.Column(db.String(255), nullable=False)
    entwentytwocity = db.Column(db.String(50), nullable=False)
    entwentytwo = db.Column(db.String(255), nullable=False)

    # ===23th day===
    twentythree_city = db.Column(db.String(50), nullable=False)
    twentythree = db.Column(db.String(255), nullable=False)
    entwentythreecity = db.Column(db.String(50), nullable=False)
    entwentythree = db.Column(db.String(255), nullable=False)

    # ===24th day===
    twentyfour_city = db.Column(db.String(50), nullable=False)
    twentyfour = db.Column(db.String(255), nullable=False)
    entwentyfourcity = db.Column(db.String(50), nullable=False)
    entwentyfour = db.Column(db.String(255), nullable=False)

    # ===25th day===
    twentyfive_city = db.Column(db.String(50), nullable=False)
    twentyfive = db.Column(db.String(255), nullable=False)
    entwentyfivecity = db.Column(db.String(50), nullable=False)
    entwentyfive = db.Column(db.String(255), nullable=False)

    # ===26th day===
    twentysix_city = db.Column(db.String(50), nullable=False)
    twentysix = db.Column(db.String(255), nullable=False)
    entwentysixcity = db.Column(db.String(50), nullable=False)
    entwentysix = db.Column(db.String(255), nullable=False)

    # ===27th day===
    twentyseven_city = db.Column(db.String(50), nullable=False)
    twentyseven = db.Column(db.String(255), nullable=False)
    entwentysevencity = db.Column(db.String(50), nullable=False)
    entwentyseven = db.Column(db.String(255), nullable=False)

    # ===28th day===
    twentyeight_city = db.Column(db.String(50), nullable=False)
    twentyeight = db.Column(db.String(255), nullable=False)
    entwentyeightcity = db.Column(db.String(50), nullable=False)
    entwentyeight = db.Column(db.String(255), nullable=False)

    # ===29th day===
    twentynine_city = db.Column(db.String(50), nullable=False)
    twentynine = db.Column(db.String(255), nullable=False)
    entwentyninecity = db.Column(db.String(50), nullable=False)
    entwentynine = db.Column(db.String(255), nullable=False)

    # ===30th day===
    thirty_city = db.Column(db.String(50), nullable=False)
    thirty = db.Column(db.String(255), nullable=False)
    enthirtycity = db.Column(db.String(50), nullable=False)
    enthirty = db.Column(db.String(255), nullable=False)


class ToursCat(db.Model):
    __tablename__ = 'tourscat'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    en_cat = db.Column(db.String(100), nullable=False)
    ru_cat = db.Column(db.String(100), nullable=False)
    day_pack = db.Column(db.Integer)

    pr = db.relationship('ToursInfo', backref='tourscat', uselist=False)

    def __repr__(self):
        return f'<ToursCat_id {ToursCat.category}>'


class ToursInfo(db.Model):
    __tablename__ = 'toursinfo'
    id = db.Column(db.Integer, primary_key=True)
    ru_loc = db.Column(db.String(100), nullable=False) #location
    en_loc = db.Column(db.String(100), nullable=False)
    adult_pr = db.Column(db.Integer) # adult price
    kids_pr = db.Column(db.Integer) # price for kids
    photos = db.Column(db.String(255), nullable=False) #photos for tours
    ru_des = db.Column(db.Text, nullable=False)  # Descriptions
    en_des = db.Column(db.Text, nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('tourscat.id')) # Foreign key for catigories from ToursCat table
    reviews = db.Column(db.Integer)

    pr = db.relationship('PackDay', backref='toursinfo', uselist=False)

    def __repr__(self):
        return f'<ToursCat_id {ToursInfo.ru_loc}>'


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    job = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.LargeBinary)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.LargeBinary)
    login = db.Column(db.String(50), nullable=False)
    psw = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean)


class Travlio(db.Model):
    __tablename__ = 'travlio'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    ru_address = db.Column(db.String(255), nullable=False)
    en_address = db.Column(db.String(255), nullable=False)
    tel1 = db.Column(db.Integer)
    tel2 = db.Column(db.Integer)
    ru_about = db.Column(db.String(255), nullable=False) #in the About page text wich contains info about company
    en_about = db.Column(db.String(255), nullable=False)
    facebook = db.Column(db.String(255), nullable=False) #links for social media
    telegram = db.Column(db.String(255), nullable=False)
    instagram = db.Column(db.String(255), nullable=False)
    youtube = db.Column(db.String(255), nullable=False)
    usd = db.Column(db.Integer)
    eur = db.Column(db.Integer)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    ru_ques = db.Column(db.String(255), nullable=False)
    en_ques = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer) # different betweeen categories of questions

    pr = db.relationship('Answer', backref='question', uselist=False)

    def __repr__(self):
        return f"<Question {Question.id}>"


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    ru_ans = db.Column(db.String(255), nullable=False)
    en_ans = db.Column(db.String(255), nullable=False)
    que_id = db.Column(db.Integer, db.ForeignKey('question.id')) # choise the answer of wich question

class Seo(db.Model):
    __tablename__='seo'
    id = db.Column(db.Integer, primary_key=True)
    main_title_ru = db.Column(db.String(255))
    main_title_en = db.Column(db.String(255))
    main_des_ru = db.Column(db.String(255))
    main_des_en = db.Column(db.String(255))

    about_title_ru = db.Column(db.String(255))
    about_title_en = db.Column(db.String(255))
    about_des_ru = db.Column(db.String(255))
    about_des_en = db.Column(db.String(255))

    tours_title_ru = db.Column(db.String(255))
    tours_title_en = db.Column(db.String(255))
    tours_des_ru = db.Column(db.String(255))
    tours_des_en = db.Column(db.String(255))

    hotels_title_ru = db.Column(db.String(255))
    hotels_title_en = db.Column(db.String(255))
    hotels_des_ru = db.Column(db.String(255))
    hotels_des_en = db.Column(db.String(255))

    article_title_ru = db.Column(db.String(255))
    article_title_en = db.Column(db.String(255))
    article_des_ru = db.Column(db.String(255))
    article_des_en = db.Column(db.String(255))

    faq_title_ru = db.Column(db.String(255))
    faq_title_en = db.Column(db.String(255))
    faq_des_ru = db.Column(db.String(255))
    faq_des_en = db.Column(db.String(255))

    contact_title_ru = db.Column(db.String(255))
    contact_title_en = db.Column(db.String(255))
    contact_des_ru = db.Column(db.String(255))
    contact_des_en = db.Column(db.String(255))

    toursdetail_title_ru = db.Column(db.String(255))
    toursdetail_title_en = db.Column(db.String(255))
    toursdetail_des_ru = db.Column(db.String(255))
    toursdetail_des_en = db.Column(db.String(255))

    hoteldetail_title_ru = db.Column(db.String(255))
    hoteldetail_title_en = db.Column(db.String(255))
    hoteldetail_des_ru = db.Column(db.String(255))
    hoteldetail_des_en = db.Column(db.String(255))