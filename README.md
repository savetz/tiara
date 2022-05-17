
# TIARA    [![Badge License]][License]

*The Internet Archive Research Assistant*

<br>

<div align = center>

---

[![Button Archive]][Internet Archive]   
[![Button Bugs]][Bugs]   
[![Button Donate]][Donate]

---

<br>


<img
    src = 'Resources/Showcase.png'
    height = 400
    title = 'Screenshot showing a sample days new items: four hits for "Pliny The Elder" and eight for "Wilamette River"'
/>
    
</div>

<br>
<br>

Daily search Internet Archive for new items matching your keywords

Searches [Internet Archive] using its full text search for new items matching the keywords you specify. Run this script once a day via crontab for daily updates about new items relevant to your ongoing research subjects. It keeps track of the items it has already found, so will only alert you to new-to-you items. The script outputs its findings to an html file, and optionally emails that file to you via SendGrid or your system mail (eg Sendmail or Postfix).


<br>
<br>

## Usage

Simply place your keywords / phrases into [`/Source/searchlist.txt`][SearchList] .

### Example

```txt
Pliny The Elder
Willamette River
Atari 1200XL computer
...
```

### Note

*Try not to use generic terms like `dogs` ,* <br>
*as this will return too many daily hits.*

<br>
<br>

##  Requirements

- The script requires read / write access to it's directory

- **[Internet Archive Command Line Tool][IACLT]**

    ```sh
    pip3 install internetarchive
    ```
    
<br>


<!----------------------------------------------------------------------------->

[Internet Archive]: https://archive.org/
[Twitter]: https://twitter.com/kaysavetz
[Donate]: https://archive.org/donate/
[IACLT]: https://github.com/jjjake/internetarchive

[SearchList]: Source/searchlist.txt
[License]: LICENSE
[Bugs]: Documentation/Bugs.md

<!--------------------------------{ Badges }----------------------------------->

[Badge License]: https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge


<!-------------------------------{ Buttons }----------------------------------->

[Button Archive]: https://img.shields.io/badge/Internet_Archive-666666?style=for-the-badge&logo=InternetArchive&logoColor=white
[Button Donate]: https://img.shields.io/badge/Donate-yellow?style=for-the-badge&logo=InternetArchive&logoColor=white
[Button Bugs]: https://img.shields.io/badge/Bugs-6A5FBB?style=for-the-badge
