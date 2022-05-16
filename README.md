
# TIARA    [![Badge License]][License]

*The Internet Archive Research Assistant*

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

## Known Issues

- Thumbnails aren't generated for all items

    *You will see the broken-image icon.*

- Full text search doesn't seem to allow exact phrase matching

    *A search such as `Pliny The Elder` may return items* <br>
    *mentioning the exact phrase but can also return ones* <br>
    *with `Pliny` on one page and `Elder` on another.*


If you find this tool useful, please [donate to Internet Archive][Donate]

![screenshot showing a sample day's new items: four hits for "Pliny The Elder" and eight for "Wilamette River"][Showcase]


<!----------------------------------------------------------------------------->

[Internet Archive]: https://archive.org/
[Twitter]: https://twitter.com/kaysavetz
[Donate]: https://archive.org/donate/
[IACLT]: https://github.com/jjjake/internetarchive

[Showcase]: Resources/Showcase.png
[License]: LICENSE

<!--------------------------------{ Badges }----------------------------------->

[Badge License]: https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge
