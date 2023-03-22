import flag
from countryinfo import CountryInfo

from FallenRobot import dispatcher
from FallenRobot import telethn as borg
from FallenRobot.events import register


@register(pattern="^/country (.*)")
async def msg(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lol = input_str
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await event.reply("Country Not Available Currently")
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = "".join(f"{p},  " for p in bb)
    area = a.get("area")
    hell = a.get("borders")
    borders = "".join(f"{fk},  " for fk in hell)
    WhAt = a.get("callingCodes")
    call = "".join(f"{what}  " for what in WhAt)
    capital = a.get("capital")
    fker = a.get("currencies")
    currencies = "".join(f"{FKer},  " for FKer in fker)
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
        po = iSo.get(hitler)
        iso += f"{po},  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)

    languages = a.get("languages")
    lMAO = "".join(f"{lmao},  " for lmao in languages)
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = "".join(f"{jerry},   " for jerry in tik)
    GOT = a.get("tld")
    lanester = "".join(f"{targaryen},   " for targaryen in GOT)
    wiki = a.get("wiki")

    caption = f"""<b><u>Information Gathered Successfully</b></u>

<b>Country Name :</b> {name}
<b>Alternative Spellings :</b> {hu}
<b>Country Area :</b> {area} square kilometers
<b>Borders :</b> {borders}
<b>Calling Codes :</b> {call}
<b>Country's Capital :</b> {capital}
<b>Country's currency :</b> {currencies}
<b>Country's Flag :</b> {okie}
<b>Demonym :</b> {HmM}
<b>Country Type :</b> {EsCoBaR}
<b>ISO Names :</b> {iso}
<b>Languages :</b> {lMAO}
<b>Native Name :</b> {nonive}
<b>Population :</b> {waste}
<b>Region :</b> {reg}
<b>Sub Region :</b> {sub}
<b>Time Zones :</b> {tom}
<b>Top Level Domain :</b> {lanester}
<b>Wikipedia :</b> {wiki}

<u>Information Gathered By {dispatcher.bot.first_name}</u>
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        link_preview=None,
    )


__help__ = """
I will give information about a country

 ❍ /country <country name>*:* Gathering info about given country
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@Farooq_is_KING](https://t.me/Farooq_is_KING)⛦⃕͜🇮🇳𓊉
"""

__mod_name__ = "🇮🇳𝐂𝐎𝐔𝐍𝐓𝐑𝐘🇮🇳"
