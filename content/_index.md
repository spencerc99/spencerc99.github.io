---
title: "ꜱᴘᴇɴᴄᴇʀ ᴄʜᴀɴɢ (っ◔◡◔)っ"
description: "Spencer is a creative technologist, developer of poetics, and dream researcher in San Francisco. He creates playful and intimate software and words to imagine alternative futures of computing."
# (っ◔◡◔)っ ♥ spencer chang ♥
---
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

<p id="expandingWork"></p>

<p id="expandingLikes"></p>


<script>
const workDescription =`
* I spend my days building
* tools for tinkers at <a id="coda" href="https://coda.io">Coda</a>,
  * tools for tinkers at <a id="coda" href="https://coda.io">Coda</a> (I built out our <a href="/posts/rituals-remixing">custom templates platform</a> and now work on the <a href="https://coda.io/packsbeta">Packs platform</a>),
    * tools for tinkers at <a id="coda" href="https://coda.io">Coda</a> (I built out our <a href="/posts/rituals-remixing">custom templates platform</a> and now work on <a href="https://coda.io/packsbeta">Packs platform</a> so that anyone can extend Coda's capabilities, maintaining an <a href="https://github.com/coda/packs-sdk">open-source SDK</a>),
* conjuring 
* soulful speculations of new futures at <a href="https://verses.xyz" id="verses">verses</a>, 
  * soulful speculations of new futures at <a href="https://verses.xyz" id="verses">verses</a> (I recently co-stewarded the creation of <b  id="pluriverse"><a href="https://pluriverse.world">pluriverse.world</a></b>),
* exploring what a new internet of <a id="tinyInternets" href="https://tiny-inter.net/">𝓽𝓲𝓷𝔂 𝓲𝓷𝓽𝓮𝓻𝓷𝓮𝓽𝓼</a> looks like
  * exploring what a new internet of <a id="tinyInternets" href="https://tiny-inter.net/">𝓽𝓲𝓷𝔂 𝓲𝓷𝓽𝓮𝓻𝓷𝓮𝓽𝓼</a>, one where <a href="https://open.substack.com/pub/spencerchang/p/ti-01-our-internet">we can make homes</a>, looks like
    * exploring what a new internet of <a id="tinyInternets" href="https://tiny-inter.net/">𝓽𝓲𝓷𝔂 𝓲𝓷𝓽𝓮𝓻𝓷𝓮𝓽𝓼</a>, one where <a href="https://open.substack.com/pub/spencerchang/p/ti-01-our-internet">we can make homes</a> and relate to others in ways that cultivate a communal space, looks like
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
// const likesDescription = `
// * I enjoy 
// * writing,
//   * <a href="/posts">writing</a> (<a href="https://spencerchang.substack.com/">personal essays</a>, software visions, poetry, and a mix of all of the above),
//     * <a href="/posts">writing</a> (<a href="https://spencerchang.substack.com/">personal essays</a>, software visions, poetry. check out my <a href="/experiments/100posts">100 posts</a> experiment, my <a href="/posts/boundless-shapeshifters">shapeshifting poem</a> or my <a href="https://spencerchang.substack.com/p/ti-01-our-internet">internet manifesto</a>),
// * reading,
//   * <a href="https://www.goodreads.com/user/show/93224420-spencer-chang">reading</a> (spec fic, short fiction, and convivial software thoughts),
// * and 
// * eating. 
//   * eating (and sharing to try more things!).
// * I also enjoy experimenting with <a href="/fits">fashion</a>, 
// * dancing,
//   * dancing (both in my room, around the kitchen, and in quiet corners of public spaces),
// * <a href="/photos">capturing moments</a>, and being 
// * in nature.
//   * in nature (or just generally exploring this beautiful world).
// `;
// TODO: support descriptors for each in the list, and have a way to "ellipsis" to add a new of the top level one
// 'in my room', 'snuggled in quiet corners', 'in public parks'
let likes = [
  ['writing'],
  ['reading'],
  ['eating'],
  ['dressing up'],
  ['dancing'],      
  ['paying attention'],      
  ['wondering'],      
  ['wandering'],      
  ['daydreaming'],      
  ['capturing moments'],
  ['being in nature'],
  ['loving people'],
  ['sipping water'],
  ['loving life'],
  ['cracking my joints'],
  ['watermelon on a hot day'],
  ['recognizing constellations'],
  ['the city skyline at night'],
  ['uncontrollable crying'],
  ['creating magic'],
  ['experimenting'],
  ['speculative infrastructure'],
  ['computational poetry'],
  ['creative technology'],
  ['agencyful computation'],
  ['alternative futures'],
  ['playful tools'],
  ['evocative writing'],
  ['imaginative fiction'],
  ['wonder'],
  ['tools for wonder'],
  ['everyday beauty'],
  ['accessible magic'],
  ['cybernetic ecology'],
  ['pluriversality'],
]
const enjoyPrompt = `<a href="https://coda.io/form/spencers-enjoy-list_dGFsXoodVB1">what do you think I'll like?</a>`;
// randomize likes
likes = likes.sort(() => Math.random() - 0.5);
likes.splice(4, 0, [enjoyPrompt]);
let likeExpandedIdx = 0;

function createLikeNode(like) {
  const likeNode = document.createElement("span");
  likeNode.innerHTML = `${like}`;
  if (likeExpandedIdx < likes.length - 1) {
    likeNode.innerHTML += ', ';
  }
  return likeNode;
}
// const likesNode = createTelescopicTextFromBulletedList(likesDescription, {textMode: TextMode.Html});
// const likesContainer = document.getElementById("expandingLikes")
// likesContainer.appendChild(likesNode);
const likesNode = document.createElement("div");
likesNode.id = 'telescope';
const onMoreNode = document.createElement("span");
onMoreNode.innerHTML = '...';
onMoreNode.addEventListener('click', onClickMore);
const likesContainer = document.getElementById("expandingLikes")
likesContainer.appendChild(likesNode);
likesNode.appendChild(document.createTextNode('A non-exhaustive list of the things I enjoy:'))
likesNode.appendChild(document.createElement("br"))
likesNode.appendChild(onMoreNode);
onMoreNode.classList.add("details");
onMoreNode.classList.add("close");


function onClickMore() {
  const likeNode = createLikeNode(likes[likeExpandedIdx]);
  likesNode.insertBefore(likeNode, onMoreNode);
  likeExpandedIdx++;
  if (likeExpandedIdx === likes.length) {
    onMoreNode.remove();
    return;
  }
}
onClickMore();

</script>

<p>
    <details>
    <summary>some things I'm proud of...</summary>
    <div>
        <ul class="noPadding">
        <li><a href="https://coda.io/packs">Packs Ecosystem</a>: A platform and ecosystem for extending the functionality of Coda by 
        connecting to external services and taking action on data. Makes Coda better achieve a promise of interoperability and being an operating layer on top of all your existing data from anywhere.</li>
        <li><a href="https://pluriverse.world">Towards a Digital Pluriverse</a>: An interactive, participatory essay proposing the "pluriverse" as a new banner for the community to rally around for how we look at imagining a "new web." It is co-created with visitors and readers of the site.</li>
        <li><a href="https://coda.io/@steve/meet-custom-templates">Custom Templates</a>: empowered anyone to create a template on Coda, a reusable and shareable set of components, to streamline common workflows, share personal tools with their team, and adopt practices from the wider community in their own doc.</li>
        <li><a href="https://tiny-inter.net">tiny internets</a>: a research inquiry on what does a more natural, soft, and quiet internet look like, one where public spaces are actively shaped by us to not only use but live in? Explored during the Interact Residency and created browser extension explroing different avenues for intimacy with beta users, including digital geocaching, commuting, and time capsules.</li>
        <li><a href="/posts/everyday-magic">Everyday Magic</a> essay for <a href="https://reboothq.substack.com/">reboot</a> on the magic of the technology and why we need to and how we make it accessible to everyone.</li>
        <li><a href="/experiments/100posts">100 mini-essays</a>: A collection of 100 posts I've written in 2021, comprising personal essays, poems, short stories, and more.</li>
        <li>My <a href="/fits">Fits Stream</a>, an auto-stream of my daily outfits.</li>
        </ul>
    </div>
    </details>
</p>

<!-- TODO: make an art page -->
Open to collaborations and chatting around <a href="https://coda.io/@spencer/tiny-internets/public-presentations-39">digital media art</a>, <a href="/experiments/100posts/future-of-tools/">speculative infrastructure</a>, and alternative <a href="https://tiny-inter.net/">internets</a>.
