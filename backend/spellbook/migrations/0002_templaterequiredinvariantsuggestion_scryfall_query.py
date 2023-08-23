# Generated by Django 4.2.4 on 2023-08-23 21:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='templaterequiredinvariantsuggestion',
            name='scryfall_query',
            field=models.CharField(blank=True, help_text='Variables supported: manavalue, mv, power, pow, toughness, tou, powtou, pt, loyalty, loy, color, c, identity, id, has, type, t, keyword, is, mana, m, devotion, produces. Operators supported: =, !=, <, >, <=, >=, :. You can compose a "and"/"or" expression made of "and"/"or" expressions, like "(c:W or c:U) and (t:creature or t:artifact)". You can also omit parentheses when not necessary, like "(c:W or c:U) t:creature". More info at: https://scryfall.com/docs/syntax.', max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Invalid Scryfall query syntax.', regex='^(?:(?:\\((?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)))))*)\\)|(?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)))))*))(?: (?:and |or )?(?:\\((?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)))))*)\\)|(?:(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy))))(?: (?:and |or )?(?:-?(?:(?:(?:c|color|id|identity|produces)(?::|[<>]=?|!=|=)|(?:has|t|type|keyword|is):)(?:[^\\s:<>!="]+|"[^"]+")|(?:m|mana|devotion)(?::|[<>]=?|!=|=)(?:\\{(?:[WUBRG](?:\\/P)?|[0-9CPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|U\\/B|U\\/R|B\\/R|B\\/G|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)(?::|[<>]=?|!=|=)(?:\\d+|(?:mv|manavalue|power|pow|toughness|tou|pt|powtou|loyalty|loy)))))*)))*)$')], verbose_name='Scryfall query'),
        ),
    ]
