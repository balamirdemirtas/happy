from modeltranslation.translator import TranslationOptions, translator


from blog.models import Post
from rent.models import Category,Product,Reservation,İndexComment
from rota.models import Rota
from sell.models import SellCategory,SellProduct
from special.models import SpecialCategory,SpecialProducts



class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)



class PostTranslationOptions(TranslationOptions):
    fields = ("title","content",)



class ProductTranslationOptions(TranslationOptions):
    fields = ('name','info','index_info',)



class RotaTranslationOptions(TranslationOptions):
    fields = ('name','rota','exit','liman',)

class SellCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


class SellProductTranslationOptions(TranslationOptions):
    fields = ('name','info','index_info','kabin','aircon','kabin_type','producer','flag','status','saleType','sale','rudder','boatHull',)


class SpecialCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


class SpecialProductsTranslationOptions(TranslationOptions):
    fields = ("title",'content','strong_content')


class İndexCommentTranslations(TranslationOptions):
    fields = ("name", 'city', 'subject','text',)

translator.register(Category,CategoryTranslationOptions)
translator.register(Post,PostTranslationOptions)
translator.register(Product,ProductTranslationOptions)
translator.register(Rota,RotaTranslationOptions)
translator.register(SellCategory,SellCategoryTranslationOptions)
translator.register(SellProduct,SellProductTranslationOptions)
translator.register(SpecialCategory,SpecialCategoryTranslationOptions)
translator.register(SpecialProducts,SpecialProductsTranslationOptions)
translator.register(İndexComment,İndexCommentTranslations)