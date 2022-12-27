---
title: "𝚜𝚙𝚎𝚗𝚌𝚎𝚛𝚌𝚑𝚊𝚗𝚐.𝚖𝚎 𝚒𝚜 𝚠𝚊𝚗𝚍𝚎𝚛𝚒𝚗𝚐"
description: "Spencer is a creative technologist, world maker, and dream researcher in San Francisco. He creates playful and intimate software and words to imagine alternative futures of computing."
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
            <!-- <li>
                <b>authentic <a href="/experiments/100posts/unstoppable-expression">expression</a></b> <br/> how do we create environments that provide a <a href="/experiments/100posts/low-pressure-contexts">low-pressure context</a> for people to fail and learn and scale that <a href="/experiments/100posts/trust">trust</a> beyond small local communities?
            </li> -->
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
* exploring what a world of <a id="tinyInternets" href="https://tiny-inter.net/">𝓽𝓲𝓷𝔂 𝓲𝓷𝓽𝓮𝓻𝓷𝓮𝓽𝓼</a>,
  * exploring what a world of <a id="tinyInternets" href="https://tiny-inter.net/">𝓽𝓲𝓷𝔂 𝓲𝓷𝓽𝓮𝓻𝓷𝓮𝓽𝓼</a>, one where <a href="/posts/our-internet">we can make homes</a>,
    * exploring what a world of <a id="tinyInternets" href="https://tiny-inter.net/">𝓽𝓲𝓷𝔂 𝓲𝓷𝓽𝓮𝓻𝓷𝓮𝓽𝓼</a>, one where <a href="/posts/our-internet">we can make homes</a> and relate to others in ways that cultivate a communal space,
* and exploring poetry, through writing, art, and
* software.
  * playful
    * playful, open
      * playful, open, and empowering
  * software (like this <a href="poems.verses.xyz">expanding poems library</a> and <a href="/pacman-poem">pacman poem</a>).
    * software (like this <a href="poems.verses.xyz">expanding poems library</a> and <a href="/pacman-poem">pacman poem</a> or my <a href="/window">wall of windows</a>).
      * software (like this <a href="poems.verses.xyz">expanding poems library</a> and <a href="/pacman-poem">pacman poem</a> or my <a href="/window">wall of windows</a> or this <a href="https://coda.io/@spencer/tiny-internets/our-internet-map-51">participatory art exhibit</a>).
`;
let node = createTelescopicTextFromBulletedList(workDescription, {textMode: TextMode.Html});
const container = document.getElementById("expandingWork")
container.appendChild(node);
// TODO: can you add hover tooltips with images and previews?
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
  ['tools for wonder'],
  ['everyday beauty'],
  ['accessible magic'],
  ['cybernetic ecology'],
  ['pluriversality'],
  ['rain drops rolling down the side of a window'],
  ["a large scarf that covers your face when it's cold outside"],
  ['warm pockets'],
  ['tender hugs'],
  ['lingering tastes'],
  ['warm lighting'],
  ['fantasizing being a blade of grass in a Hayao Miyazaki film'],
  ['stardust and shoreless seeds'],
  ['unexpected light'],
  ['unexpected mediums'],
  ['folk practices'],
  ['daily rituals'],
  ['dreaming'],
  ["art that doesn't take itself too seriously"],
  ["creating things"],
  ["making new stuff from old stuff"],
  ["laughing with friends"],
  ["sharing food"],
  ["hole-in-the-walls"],
  ["complimenting people on their outfits"],
  ["getting complimented on my outfit"],
  ["receiving a reply on my newsletter"],
  ["receiving an email from a visitor to my site"],
  ["a full water bottle"],
  ["sufficiently chapsticked lips"],
  ["worn books"],
  ["marginalia"],
  ["soulful things"],
  ["people who look at the world"],
  ["walking aimlessly"],
  ["running under 6 miles in nice weather"],
  ["taking care of things"],
  ["cultivating life"],
  ["naming"],
  ["sitting with the unknown"],
  ["laying under the stars"],
  ["watching meteor showers"],
  ["making things up and committing to the bit"],
]
const enjoyPrompt = `<a href="https://coda.io/form/spencers-enjoy-list_dGFsXoodVB1">what do you think I'll like?</a>`;
// randomize likes
likes = likes.sort(() => Math.random() - 0.5);
likes.splice(4, 0, [enjoyPrompt]);
let likeExpandedIdx = 0;

function createLikeNode(like) {
  const likeNode = document.createElement("span");
  likeNode.classList.add('likeItem')
  likeNode.innerHTML = `${like}`;
  if (likeExpandedIdx < likes.length - 1) {
    likeNode.innerHTML += ', ';
  } 
  if (likeExpandedIdx === likes.length - 2) {
    likeNode.innerHTML += 'and ';
  } 
  return likeNode;
}
// const likesNode = createTelescopicTextFromBulletedList(likesDescription, {textMode: TextMode.Html});
// const likesContainer = document.getElementById("expandingLikes")
// likesContainer.appendChild(likesNode);
const likesNode = document.createElement("div");
likesNode.id = 'telescope';
const onMoreNode = document.createElement("div");
onMoreNode.style = "display: inline-block;"
onMoreNode.setAttribute('role', 'button')
onMoreNode.setAttribute('tabindex', '0')
onMoreNode.innerHTML = 'and...';
onMoreNode.addEventListener('click', onClickMore);
onMoreNode.addEventListener('keydown', onKeyDown);
const likesContainer = document.getElementById("expandingLikes")
likesContainer.appendChild(likesNode);
likesNode.appendChild(document.createTextNode('A non-exhaustive list of the things I enjoy:'))
likesNode.appendChild(document.createElement("br"))
likesNode.appendChild(onMoreNode);
onMoreNode.classList.add("details");
onMoreNode.classList.add("close");


function onKeyDown(e) {
  if (event.key === 'Enter' || event.key === ' ') {
    onClickMore();
    e.preventDefault();
  }
}

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
