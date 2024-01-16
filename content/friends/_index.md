---
title: friends
---

<div id="friends">
    <script>
        fetch(
            "https://raw.githubusercontent.com/spencerc99/poeticomp-friends/main/webring.json"
        )
            .then((c) => c.json())
            .then((webring) => {
                for (const friend of webring) {
                    if (friend.url.includes('spencerchang.me')) continue;
                    const container = document.createElement('div');
                    container.classList.add('friendContainer');
                    const frameElement = document.createElement('iframe');
                    frameElement.src = friend.url;
                    const { height, width } = friend.dimensions || {};
                    frameElement.width = width;
                    frameElement.height = height;
                    const plaque = document.createElement('a');
                    plaque.innerText = `${friend.name || ''}`;
                    plaque.href = friend.url;
                    container.append(frameElement, plaque);
                    friends.appendChild(container);
                }
            });        
    </script>
</div>

<br/>
<br/>
<div style="text-align: center">
Send me a letter if you'd like to join this circle of poeticomp friends.
</div>

