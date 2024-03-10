---
title: "who is spencer?"
description: programmer, artist, writer, internet imagineer, computational poet
---
<!-- TODO: make this rotating bios that are live hooked up to a data source -->

Spencer creates infrastructure for a more playful, light, and communal internet in the form of new interaction mediums, website environments, open protocols, and local-first applications. He does this through creating (tools|games|spaces) that push how we're allowed to dictate digital places and objects, making site-specific net art that question our assumptions of what websites are and who we are when we visit them, and writing about his findings and the emotional journey of this independent path.

They find it hard to describe themselves, so they prefer to reveal who they are through the things they care about. They've designed and built products at <a id="square" href="http://squareup.com/">Square</a>, <a href="https://www.airbnb.com/" id="airbnb">Airbnb</a>, and most recently <a id="coda" href="https://coda.io">Coda</a> and <a href="https://verses.xyz" id="verses">verses</a>. Their art has been shown at the [de Young Museum](https://www.famsf.org/), [CultureHub](https://www.culturehub.org/events/inspect-elements), and [SFPC](https://sfpc.study/), and their work has been featured in [Frieze](https://www.frieze.com/) and [MIT Technology Review](https://www.technologyreview.com/2023/12/21/1084525/internet-whimsy-html-energy/). Their words have been published in [Kernel Magazine](https://www.kernelmag.io/), [Syllabus Project](https://syllabusproject.org/syllabus-for-taking-an-internet-walk/), and regularly in their newsletter [spencer's paradoxes](https://spencerchang.substack.com/).

Some other explorations that don't quite fit into these boxes include [baristaing](https://twitter.com/spencerc99/status/1629293479825375233), [site-specific digital media installations](https://twitter.com/MatthewWSiu/status/1623910442921000961?s=20), [unusual mediums](https://twitter.com/spencerc99/status/1744415360089280835) for computing, and communal sites for connection.

<!-- <div class="aboutContent">
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
<p>welcome to my digital home., why did i make this website? why is it so important? why did i make this website? why is it so important? why did i make this website? why is it so important?</p>
<img src="/assets/spencer_real_person.png"/>
</div> -->

<p id="expandingLikes"></p>

<!-- Likes logic -->
<script>
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
  ["saying hi to the moon"],
  ["collecting sunset colors"],
  ["smiskis"],
  ["Noguchi lamps"],
  ["oranges (the color)"],
  ["oranges (the fruit)"],
  ["oranges (the mood)"],
  ["a crisp wifi connection"],
  ["overlapping voices in a cafe"],
  ["a hot cortado (oat milk please!)"],
  ["sliced watermelon on a hot summer day"],
  ["feeling the wind on my cheek while biking"],
  ["plants (that are easy to keep alive)"],
  ["San Francisco's air"],
  ["New York's energy"],
  ["noticing a stranger's smile on a bus"],
  ["things made with love"],
  ["anything soft and fuzzy"],
  ["aeropress coffee"],
  ["fast wifi"],
  ["dance circles in playgrounds at night"],
  ["Yohji Yamamoto clothing"],
  ["bags in bags"],
]
const enjoyPrompt = `<a href="https://coda.io/form/spencers-enjoy-list_dGFsXoodVB1">what do you think I'll like?</a>`;
// randomize likes
likes = likes.sort(() => Math.random() - 0.5);
likes.splice(12, 0, [enjoyPrompt]);
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
const likesNode = document.createElement("div");
likesNode.id = 'telescope';
const onMoreNode = document.createElement("div");
onMoreNode.style = "display: inline-block;"
onMoreNode.setAttribute('role', 'button')
onMoreNode.setAttribute('tabindex', '0')
onMoreNode.setAttribute('title', 'click me to see more! try tabbing to me and using enter or space to go even faster!')
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
// start with 3 open
onClickMore();
onClickMore();
onClickMore();
onClickMore();

</script>
