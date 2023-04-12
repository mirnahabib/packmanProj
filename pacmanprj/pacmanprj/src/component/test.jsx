import React, { useState } from "react";

function Test() {
  const [data, setData] = useState(null);
  const [Cat, setCat] = useState("");
  const [Query, setQuery] = useState("");

  const fetchData = async () => {
    try {
      //"https://api.escuelajs.co/api/v1/products"
      //http://localhost:5000/api/search/general/playstation

      /* //fake api Cat: v1 ,Query: products
      const response = await fetch(
        `https://api.escuelajs.co/api/${Cat}/${Query}`
      ); */

      //our api
        const response = await fetch(
          `/api/search/${Cat}/${Query}`
        );

      const jsonData = await response.json();
      setData(jsonData);
      console.log(data)
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <section>
      <form>
        <label>
          Cat:
          <input
            type="text"
            id="Cat"
            value={Cat}
            onChange={(e) => setCat(e.target.value)}
          />
        </label>
        <label>
          Query:
          <input
            type="text"
            id="Query"
            value={Query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </label>
      </form>
      <button onClick={fetchData}>Fetch Data</button>

      {/* our api */}
      
      {/* {data && (
        <div className="container pt-5">
        <div className="row">
          {data.map((item) => {
          return (
            <div
              className="card d-flex flex-column justify-content-between col-lg-3 col-12 gx-2 shadow"
              style={{ border: "solid 5px", borderRadius: "15px" }}
            >
              <img
                src={item.Img}
                className="card-img-top w-50 mx-auto mt-3"
                alt={item.Title}
              />
              <div className="card-body d-flex flex-column justify-content-end">
                <a href={item.Link} className="card-title">
                  {item.Title}
                </a>
                <h2 className="fw-bolder fs-3 text-center">{item.Price}</h2>
                <small>{item.Shop}</small>
              </div>
            </div>
          );
        })}
        </div>
      </div>
      )} */}


      {/* the fake api
      {data && (
        <ul>
          {data.map((item) => (
            <div
              className="card d-flex flex-column justify-content-between col-lg-3 col-12 gx-2 shadow"
              style={{ border: "solid 5px", borderRadius: "15px" }}
            >
              <img
                src={item.category.image}
                className="card-img-top w-50 mx-auto mt-3"
                alt={item.title}
              />
              <div className="card-body d-flex flex-column justify-content-end">
                <a href={item.description} className="card-title">
                  {item.Title}
                </a>
                <h2 className="fw-bolder fs-3 text-center">{item.price}</h2>
                <small>{item.title}</small>
              </div>
            </div>
          ))}
        </ul>
      )} */}
    </section>
  );
}

export default Test;
