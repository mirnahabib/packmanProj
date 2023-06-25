import React, { useEffect, useState } from "react";
import { Row , Container} from "react-bootstrap";
import Productcard from "./productcard";
import { Logos } from "./logos";


export default function Favourites() {
  const [favList, setfavList] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        let response = await fetch(`/api/favourites/`);
        const jsonData = await response.json();
        setfavList(jsonData.favlist);
        console.log(jsonData.favlist);
        console.log(jsonData.favlist[0].currentPrice)
      } catch (error) {
        console.error(error);
      }
    })();
  }, []);

  return (
    <div>
      <Container className="text-center Font" width="10px">
      <Row sm={1} md={1} lg={1} >
        {favList.map((product) => (
          <div className="col p-3 my-3 border border-warning">
            <p>{product.title}</p>
           
            <p>{product.currentPrice} EGP</p>
            <a href={product.link}>
              <img   width= "200px" src={product.img} alt={product.title}></img>
            </a>
            {/* <small>{product.store}</small> */}
            
            <p><img 
                  className=""
                  src={Logos.get(product.store)}
                  alt={product.store}
                  height="35em"
                /> </p>
          </div>
        ))}
        </Row>
      </Container>
    </div>
    
      // <div className=" row position-absolute top-50 start-50 translate-middle Font align-items-center justify-content-center text-center">
      //   <div className="row">
      //     <div className="col-12 ">
      //     <Row sm={1} md={3} lg={1} className="g-4">
      //     {favList.map((product) => (
           
            
      //         <div className="p-3 my-3 border border-warning">
                 
      //           <p>{product.title}</p>
      //           <p>{product.currentPrice} EGP</p>
      //           <a href={product.link}><img src ={product.img} alt={product.title}></img></a>
      //           <small>{product.store}</small>
      //         </div>
      //       ))}
      //     </Row>
      //     </div>
      //   </div>
      // </div>
    
  );
}
