from flask import render_template, request, Blueprint
from handblog.models import Posts
from handblog.posts.form import SearchForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # 從資料庫獲取文章
    page = request.args.get('page', 1 , type=int)
    posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("posts.html", posts=posts)

@main.context_processor
def base():
    form = SearchForm()
    return dict(form=form)
