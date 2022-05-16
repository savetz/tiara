
# TIARA    [![Badge License]][License]

*The Internet Archive Research Assistant*

<br>

<div align = center>

<img
    src = 'Resources/Showcase.png'
    height = 400
    title = 'Screenshot showing a sample days new items: four hits for "Pliny The Elder" and eight for "Wilamette River"'
/>
    
<br>

---

[![Button Bugs]][Bugs]   
[![Button Donate]][Donate]

---
    
</div>

<br>

The Internet Archive Research Assistant - Daily search Internet Archive for new items matching your keywords

Searches [Internet Archive] using its full text search for new items matching the keywords you specify. Run this script once a day via crontab for daily updates about new items relevant to your ongoing research subjects. It keeps track of the items it has already found, so will only alert you to new-to-you items. The script outputs its findings to an html file, and optionally emails that file to you via SendGrid or your system mail (eg Sendmail or Postfix).

Put your keywords in searchlist.txt, one search term per line. Very general terms (like "dogs") provide too many daily hits to be useful. More specific phrases work better.

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

[License]: LICENSE
[Bugs]: Documentation/Bugs.md

<!--------------------------------{ Badges }----------------------------------->

[Badge License]: https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge


<!-------------------------------{ Buttons }----------------------------------->

[Button Donate]: https://img.shields.io/badge/Donate-yellow?style=for-the-badge&logo=InternetArchive&logoColor=white
[Button Bugs]: https://img.shields.io/badge/Bugs-6A5FBB?style=for-the-badge
