from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="vanilla",
    size="medium",
    rating=7,
    image="https://joyfoodsunshine.com/wp-content/uploads/2021/12/best-vanilla-cupcakes-recipe-1x1-1.jpg"
)

c4 = Cupcake(
    flavor="red velvet",
    size="large",
    rating=9,
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8zFuv0IyyCifWwXWsIFsWa1ErL56Qu1DeihN9a5ux3Oj9ZLHTviKzcy74icx183jOdic&usqp=CAU"
)

c5 = Cupcake(
    flavor="guanabana",
    size="extra large",
    rating=10,
    image="https://img-global.cpcdn.com/recipes/76787e8107a3e101/400x400cq70/photo.jpg"
)

db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()