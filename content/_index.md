---
title: "Spencer Chang | creative technologist, developer of poetics, dream researcher"
description: "Spencer is a creative technologist, developer of poetics, and dream researcher in San Francisco. He creates playful and intimate software and words to imagine alternative futures of computing."
---

<i>creative technologist, developer of poetics, dream researcher</i>

<p>
    <details>
        <summary>Dreaming, wandering, laughing, and thinking about...</summary>
        <div>
            <ul class="noPadding">
            <li>
                <b>creative agency</b> <br/> how we can give users more <a href="/posts/take-back-the-future-response">agency</a> in the software they use or are used by every day and what does a healthy relationship with <a href="/posts/technology-paradox">technology look like</a>?
            </li>
            <li>
                <b><a href="https://mmm.page/helena.soft_tech">soft tech</a></b> <br/> how do we create software that encourages tinkering and authentic expression, where making crazy connections is necessary rather than a nuisance?
            </li>
            <li>
                <b>people over systems</b> <br/> what sort of systems do we need to create a society that cares about enabling every person to live with the <a href="/experiments/100posts/privilege-of-dreams">privilege to pursue their dreams</a> and create something that they can truly own?
            </li>
            <li>
                <b>authentic <a href="/experiments/100posts/unstoppable-expression">expression</a></b> <br/> how do we create environments that provide a <a href="/experiments/100posts/low-pressure-contexts">low-pressure context</a> for people to fail and learn and scale that <a href="/experiments/100posts/trust">trust</a> beyond small local communities?
            </li>
            <li>
                <b>living fully</b> <br/> how do we live more fully and <a href="/experiments/100posts/intensity">intensely</a> and learn to trust ourselves to <a href="/experiments/100posts/opportunity">express ourselves</a> without caveats?
            </li>
            </ul>
        </div>
    </details>
</p>

<p id="expandingLikes"></p>

<p id="expandingWork"></p>

<script>
const workDescription =`
* I spend my days building
* tools for tinkers at <a id="coda" href="https://coda.io">Coda</a>,
  * tools for tinkers at <a id="coda" href="https://coda.io">Coda</a> (I built out our <a href="/posts/rituals-remixing">custom templates platform</a> and now work on the <a href="https://coda.io/packsbeta">Packs platform</a>),
    * tools for tinkers at <a id="coda" href="https://coda.io">Coda</a> (I built out our <a href="/posts/rituals-remixing">custom templates platform</a> and now work on <a href="https://coda.io/packsbeta">Packs platform</a> so that anyone can extend Coda's capabilities, maintaining an <a href="https://github.com/coda/packs-sdk">open-source SDK</a>),
* conjuring 
* soulful speculations of new futures at <a href="https://verses.xyz" id="verses">verses</a>, 
  * soulful speculations of new futures at <a href="https://verses.xyz" id="verses">verses</a> (I recently co-stewarded the creation of <b  id="pluriverse"><a href="https://pluriverse.world">pluriverse.world</a></b>),
* and exploring poetry, through writing, art, and
* software.
  * open
    * open, playful
      * open, playful, and empowering
  * software (like this <a href="https://github.com/jackyzha0/telescopic-text">expanding text</a> and <a href="">shapeshifting poem</a>).
    * software (like this <a href="">expanding text</a> and <a href="/posts/boundless-shapeshifters">shapeshifting poem</a> or my <a href="/fits">fits stream</a>).
`;
let node = createTelescopicTextFromBulletedList(workDescription, {textMode: TextMode.Html});
const container = document.getElementById("expandingWork")
container.appendChild(node);
// TODO: can you add hover tooltips with images and previews?
const likesDescription = `
* I like 
* writing,
  * <a href="/writing">writing</a> (<a href="https://spencerchang.substack.com/">personal essays</a>, software essays, and poetry),
    * <a href="/writing">writing</a> (personal essays—like my <a href="/experim
    * ents/100posts">100 mini-essays project</a>, software essays, and poetry),
* reading,
  * <a href="https://www.goodreads.com/user/show/93224420-spencer-chang">reading</a> (spec fic, short fiction, and convivial software thoughts),
* and 
* eating. 
  * eating (and sharing to try more things!).
* I also enjoy experimenting with <a href="/fits">fashion</a>, 
* dancing,
  * dancing (both in my room, around the kitchen and I <a href="https://coda.io/@spencer/spencer-wrapped-2021/activity-13#_luL9E">guess live</a>),
* <a href="/photos">capturing moments</a>, and being 
* in nature.
  * in nature (or just generally exploring this beautiful world).
`;
const likesNode = createTelescopicTextFromBulletedList(likesDescription, {textMode: TextMode.Html});
const likesContainer = document.getElementById("expandingLikes")
likesContainer.appendChild(likesNode);
</script>

<p>
    <details>
    <summary>I'm proud of...</summary>
    <div>
        <ul class="noPadding">
        <li><a href="https://pluriverse.world">Towards a Digital Pluriverse</a>: An interactive, participatory essay proposing the "pluriverse" as a new banner for the community to rally around for how we look at imagining a "new web." It is co-created with visitors and readers of the site.</li>
        <li><a href="/experiments/100posts">100 mini-essays</a>: A collection of 100 posts I've written in 2021, comprising personal essays, poems, short stories, and more.</li>
        <li><a href="/posts/everyday-magic">Everyday Magic</a> essay for <a href="https://reboothq.substack.com/">reboot</a> on the magic of the technology and why we need to and how we make it accessible to everyone.</li>
        <li>My <a href="/fits">Fits Stream</a>, an auto-stream of my daily outfits.</li>
        </ul>
    </div>
    </details>
</p>
