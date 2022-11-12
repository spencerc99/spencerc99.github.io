# Spencer's Digital Garden Home

This is v3 of my website.

You can see the final product at https://spencerchang.me

---

Hi there! 👋

I'm Spencer and this is my personal website built in Hugo.

I designed this site with legibility and a delightful reading experience at the forefront, and at the same time, tried to insert playful notes of personality throughout such as with the font/icon change to denote fictional works. 

I've also designed this site to be friendly to sharing and gaining traffic by ensuring unfurls and embeds grab the proper attributes as well as adding in Google Analytics.

The site is automatically deployed to "spencerchang.me" via Github Pages.

This is open source to encourage others to make and explore their own personal websites, but I'd appreciate attribution and proper credit if you use my code or designs. Thanks!

# Fits Stream
I have a [Fits Stream](https://spencerchang.me/fits) that auto-uploads my outfits of the day from an Apple Photos album to my website in a nicely formatted way. You can see all the logic for this in `upload-fits.sh` and `data/fits.json`. This uses [osxphotos]() to export all my photos and post-process them into a JSON file for consumption. I'm inspired by the [Baked Data Architecture](https://simonwillison.net/2021/Jul/28/baked-data/) for this model (although I didn't know that was the name that had been coined for it when I embarked on this journey) so that I don't have to spin up a whole backend and "database" to handle this simple use case.

I also use this simple [Siri Shortcut]( https://www.icloud.com/shortcuts/004c7a9f6c73469783dd44613c453486) that I get reminded of at noon everyday to select a recent photo to add to my "fits" album that `osxphotos` extracts from.

# Design 
I'm inspired by several websites and people for this site. A non-exhaustive list in my [are.na channel](https://www.are.na/spencer-chang/textured-websites)

# Analytics
This site is set up with Google Analytics using the Hugo GA shortcode. I also augmented this with (this repo)[https://github.com/googleanalytics/autotrack] which adds additional GA tracking.
