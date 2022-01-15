from flask import render_template,request,Blueprint
# from structure.models import User,About,Price, WebFeature,Faq,Testimonial,Team,Appearance,Block
# # from structure.team.views import team
# from structure.web_features.forms import WebFeatureForm
# from structure.team.forms import UpdateTeamForm
# from structure.about.forms import UpdateAboutForm
# from structure.faq.forms import FaqForm
# from structure.pricing.forms import PriceForm
# from structure.testimonial.forms import TestimonialForm
# from structure.about.forms import AboutForm
# from structure.block.forms import BlockForm
# from sqlalchemy.orm import load_only
from flask_login import login_required
# from structure.appearance.forms import AppearanceForm
# from structure.block.forms import BlockForm
# from structure.appearance.views import appearance
# from structure.models import Appearance
core = Blueprint('core',__name__)

@core.route('/')
@login_required
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
 
    return render_template('index.html')
# @core.route('/base')
# def base():
#     '''
#     Example view of any other "core" page. Such as a info page, about page,
#     contact page. Any page that doesn't really sync with one of the models.
#     '''
#     about = About.query.all()
#     return render_template('base.html',about=about)


# @core.route('/hmsui')
# def hmsui():
#     '''
#     Example view of any other "core" page. Such as a info page, about page,
#     contact page. Any page that doesn't really sync with one of the models.
#     '''

#     page = request.args.get('page', 1, type=int)
#     web_features = WebFeature.query.order_by(WebFeature.date.desc()).paginate(page=page, per_page=10)
#     about = About.query.get(1)
#     price = Price.query.all()
#     faq = Faq.query.all()
#     testimonial = Testimonial.query.all()
#     team= Team.query.all()
#     serv = Price.features
#     Blockform= BlockForm()
#     team= Team.query.all()
#     block= Block.query.all()
#     Appearanceform = AppearanceForm()
#     appearance=Appearance.query.all()
#     # services=[]
#     # service= serv.split(',')
#     # services.append(service)
#     return render_template('base2.html',web_features=web_features, about=about,pricing=price,faq=faq,testimonial=testimonial,team=team,serv=serv,Blockform=Blockform,appearance=appearance,Appearanceform=Appearanceform,block=block)



# @core.route('/editui')
# @login_required
# def editui():
#     '''
#     Example view of any other "core" page. Such as a info page, about page,
#     contact page. Any page that doesn't really sync with one of the models.
#     '''
#     Webfeatureform= WebFeatureForm()
#     Teammateform = UpdateTeamForm()
#     Faqform = FaqForm() 
#     Testimonialform = TestimonialForm()
#     Pricingform = PriceForm()
#     Aboutform = AboutForm()
#     page = request.args.get('page', 1, type=int)
#     web_features = WebFeature.query.order_by(WebFeature.date.desc()).paginate(page=page, per_page=10)
#     about = About.query.get(1)
#     price = Price.query.all()
#     faq = Faq.query.all()
#     Blockform= BlockForm()
#     testimonial = Testimonial.query.all()
#     team= Team.query.all()
#     block= Block.query.all()
#     Appearanceform = AppearanceForm()
#     appearance=Appearance.query.all()
#     # for appearances in appearance:
#     #         appearance=Appearance.query.all()
#     #         Appearanceform = AppearanceForm()
#     #         Appearanceform.title_color.data = appearances.title_color
#     #         Appearanceform.subtitle_color.data = appearances.subtitle_color
#     #         Appearanceform.paragraph_color.data = appearances.paragraph_color
#     #         Appearanceform.title_font.data = appearances.title_font
#     #         Appearanceform.subtitle_font.data = appearances.subtitle_font
#     #         Appearanceform.paragraph_font.data = appearances.paragraph_font
#     #         Appearanceform.title_size.data = appearances.title_size
#     #         Appearanceform.subtitle_size.data = appearances.subtitle_size
#     #         Appearanceform.paragraph_size.data = appearances.paragraph_size
#     #         Appearanceform.bootstrap_class1.data = appearances.bootstrap_class1
#     #         Appearanceform.bootstrap_class2.data = appearances.bootstrap_class2
#     #         Appearanceform.bootstrap_class3.data = appearances.bootstrap_class3


#     # fields = ['id']
#     # data = Testimonial.options(load_only(*fields)).all()
#     emplist = []
#     for faqs in faq:
#         emplist.append("row:" +str(faqs.id))
#     print(emplist)


#     templist = []
#     for testimonials in testimonial:
#         templist= "row:" +str(testimonials.id)
#     #     templist.append("row:" +str(testimonials.id))
#     # print(templist)



#     print(faq)
#     context={
#         'about':about,
#         'web_features':web_features,
#         'price':price,
#         'faq':faq,
#         'testimonial':testimonial,
#         'team':team,
#     }

#     serv = Price.features
#     # services=[]
#     # service= serv.split(',')
#     # services.append(service)
#     return render_template('editui.html',block = block,web_features=web_features,about=about,webfeatureform = Webfeatureform,teammateform=Teammateform,faqform = Faqform,testimonialform=Testimonialform,priceform=Pricingform,aboutform=Aboutform,team=team,pricing=price,faq=faq,testimonial=testimonial,templist=templist,emplist=emplist,blockform=Blockform,appearanceform=Appearanceform,appearance=appearance)
#     # return render_template('info.html',context=context,faq=faq)
