---
title: "latest from spencer"
---

<script>
    // redirect to the latest post from the newsletter RSS feed
    const newsletterFeedUrl = 'https://spencerchang.substack.com/feed';
    fetch(`http://api.rss2json.com/v1/api.json?rss_url=${newsletterFeedUrl}`)
        .then(response => {
             return response.json();})
        .then(data => {
            document.querySelector('#latestRedirect').setAttribute('href', data.items[0].link);
            window.location.replace(data.items[0].link)
        });

</script>


<p>
you should be redirected soon, but if not head <a id="latestRedirect" href="">here</a>
</p>
