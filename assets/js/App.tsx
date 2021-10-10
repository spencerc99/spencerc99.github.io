// we dont need this for now
// import * as React from "react";
// import * as ReactDOM from "react-dom";
// import {useEffect, useState} from "react"
// import * as fitsData from '../../content/fits/fits.json';
// console.log(fitsData);

// interface Props {
//   title: string;
//   imgSrc: string;
//   description: string;
//   date: string;
//   idx: number;
// }

// function PhotoCard({ title, imgSrc, description, date, idx }: Props) {
//   return (
//     <div className="photoCard">
//       <h3>
//         {idx+1} - {title}
//       </h3>
//       <img src={imgSrc} />
//       <p>{description}</p>
//       <span className="photoCardDate">{date}</span>
//     </div>
//   );
// }


// function Fits() {
//   const [fits, setFits] = useState<undefined | any[]>();
//   console.log(fitsData)
//   useEffect(async () => {
//     const fitsRaw = await fetch("./fits.json")
//     console.log(fitsRaw);
//     const fitsJson = await fitsRaw.json()
//     setFits(fitsJson);
//   })

//   if (!fits) {
//     return "Loading";
//   }
  
//   return <div>
//     {fits.map((f,idx) => <PhotoCard key={idx} {...f} idx={idx}/>)}
//   </div>
// }

// ReactDOM.render(<Fits/>, document.getElementById("fitsContainer"))
