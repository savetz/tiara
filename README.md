# tiara
The Internet Archive Research Assistant - Daily search Internet Archive for new items matching your keywords

by [Kay Savetz](https://twitter.com/kaysavetz), May 2021. 

Searches [Internet Archive](https://archive.org/) using its full text search for new items matching the keywords you specify. Run this script once a day via crontab for daily updates about new items relevant to your ongoing research subjects. It keeps track of the items it has already found, so will only alert you to new-to-you items. The script outputs its findings to an html file, and optionally emails that file to you via SendGrid or your system mail (eg Sendmail or Postfix).

Put your keywords in searchlist.txt, one search term per line. Very general terms (like "dogs") provide too many daily hits to be useful. More specific phrases work better.

Dependency: [Internet Archive command line tool](https://github.com/jjjake/internetarchive) (Install with pip install internetarchive)
The script also requires read-write access to the directory it lives in.

Issue: Internet Archive cannot generate thumbnails for all items. In these cases, you may see a broken image icon.
Issue: Internet Archive's full text search doesn't seem to allow exact phrase matching. So a search for "Pliny The Elder" may turn up items mentioning Pliny The Younger, or with "Pliny" on one page and "elder" on another.

If you find this tool useful, please [donate to Internet Archive](https://archive.org/donate/)

![screenshot showing a sample day's new items: four hits for "Pliny The Elder" and eight for "Wilamette River"](screenshot1.png)
