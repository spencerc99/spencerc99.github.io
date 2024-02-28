---
title: "cursor watching"
emojis: ["👁️"]
---


this link will activate at 9:00PM EST on Saturday, March 2nd.

<div id="time" style="font-size: 3em; font-weight: bold; display: flex; justify-content: center;"></div>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<script>
    const targetDate = new Date("March 2, 2024 21:00:00 EST");
    const time = document.getElementById("time");
    const updateCountdown = () => {
        const now = new Date();
        const timeLeft = targetDate - now;
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = days * 24 + Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
        time.innerText = `${padLeft(hours, '0', 2)}:${padLeft(minutes, '0', 2)}:${padLeft(seconds, '0', 2)}`;
    };
    function padLeft(strInp, pad, num) {
        let str = strInp.toString();
        while (str.length < num) {
            str = pad + str;
        }
        return str;
    }
    updateCountdown();
    setInterval(updateCountdown, 1000);
</script>
