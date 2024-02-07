# Generated by Django 5.0.1 on 2024-01-19 13:36

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0012_alter_variant_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='variantsuggestion',
            name='spoiler',
            field=models.BooleanField(default=False, help_text='Is this combo a spoiler?', verbose_name='is spoiler'),
        ),
        migrations.AlterField(
            model_name='template',
            name='scryfall_query',
            field=models.CharField(help_text='Variables supported: mv, manavalue, power, pow, toughness, tou, pt, powtou, loyalty, loy, c, color, id, identity, produces, has, t, type, keyword, is, o, oracle, function, otag, oracletag, oracleid, m, mana, devotion.\nOperators supported: =, !=, <, >, <=, >=, :.\nYou can compose a "and"/"or" expression made of "and"/"or" expressions, like "(c:W or c:U) and (t:creature or t:artifact)".\nYou can also omit parentheses when not necessary, like "(c:W or c:U) t:creature".\nCard names are only supported if wrapped in double quotes and preceded by an exclamation mark (!) in order to match the exact name, like !"Lightning Bolt".\nYou can negate any expression by prepending a dash (-), like "-t:creature".\nMore info at: https://scryfall.com/docs/syntax.\n', max_length=1024, validators=[django.core.validators.RegexValidator(message='Invalid Scryfall query syntax.', regex='^(?:(?:\\((?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*)\\)|(?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*))(?: (?:and |or )?(?:\\((?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*)\\)|(?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*)))*)$')], verbose_name='Scryfall query'),
        ),
        migrations.AlterField(
            model_name='templaterequiredinvariantsuggestion',
            name='scryfall_query',
            field=models.CharField(blank=True, help_text='Variables supported: mv, manavalue, power, pow, toughness, tou, pt, powtou, loyalty, loy, c, color, id, identity, produces, has, t, type, keyword, is, o, oracle, function, otag, oracletag, oracleid, m, mana, devotion.\nOperators supported: =, !=, <, >, <=, >=, :.\nYou can compose a "and"/"or" expression made of "and"/"or" expressions, like "(c:W or c:U) and (t:creature or t:artifact)".\nYou can also omit parentheses when not necessary, like "(c:W or c:U) t:creature".\nCard names are only supported if wrapped in double quotes and preceded by an exclamation mark (!) in order to match the exact name, like !"Lightning Bolt".\nYou can negate any expression by prepending a dash (-), like "-t:creature".\nMore info at: https://scryfall.com/docs/syntax.\n', max_length=1024, null=True, validators=[django.core.validators.RegexValidator(message='Invalid Scryfall query syntax.', regex='^(?:(?:\\((?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*)\\)|(?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*))(?: (?:and |or )?(?:\\((?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*)\\)|(?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+"))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is|o|oracle|function|otag|oracletag|oracleid):!?)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))|!"[^"]+")))*)))*)$')], verbose_name='Scryfall query'),
        ),
        migrations.AlterField(
            model_name='variantsuggestion',
            name='other_prerequisites',
            field=models.TextField(blank=True, help_text='Other prerequisites for this combo.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='variantsuggestion',
            name='suggested_by',
            field=models.ForeignKey(blank=True, editable=False, help_text='User that suggested this combo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suggestions', to=settings.AUTH_USER_MODEL),
        ),
    ]