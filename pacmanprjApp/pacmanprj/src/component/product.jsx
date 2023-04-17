import React, { useState } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import Image from "react-bootstrap/Image";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import IconSearch from "./imgs/search";
import logo from "./imgs/pacman.png";
import "./css/style.css";
export default function Product() {
  const [products, setProducts] = useState(null);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("Category");

  const handleCat = (e) => {
    setCategory(e);
  };
  const fetchData = async () => {
    try {
      const response = await fetch(`/api/search/${category}/${query}`);
      const jsonData = await response.json();
      setProducts(jsonData.jsonresult);
    } catch (error) {
      console.error(error);
    }
    console.log(products);
    console.log(`${query} and the ${category}`);
  };

  return (
    <div className="">
      {!products && (
        <div className=" row position-absolute top-50 start-50 translate-middle Font align-items-center justify-content-center text-center">
          {/* <Image src={logo} fluid /> */}
          <div className="row heartbeat">
            <div className="col-12 ">
              <h3 className="pb-3 mt-3  ">Find what you are looking for</h3>
            </div>
          </div>

          <div className="row">
            <div className="col-lg-9 col-12">
              <InputGroup className="mb-3">
                <Form.Control
                  className=""
                  placeholder="Search..."
                  aria-label="Text input with dropdown button"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                />
                <IconSearch className="mt-2 ms-2" />
              </InputGroup>
            </div>
            <div className="col-lg-3  col-12">
              <DropdownButton
                title={category}
                id="category"
                onSelect={handleCat}
                align="end"
              >
                <Dropdown.Item eventKey="general">General</Dropdown.Item>
                <Dropdown.Item eventKey="grocery">Grocery</Dropdown.Item>
                <Dropdown.Item eventKey="clothes">Clothes</Dropdown.Item>
              </DropdownButton>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-3 col-12"></div>
            <div className="col-lg-6 pt-lg-0 pt-3 col-12">
              <button
                onClick={fetchData}
                type="button"
                className="btn btn-secondary"
              >
                Find My Product!
              </button>
            </div>
            <div className="col-lg-3 col-12"></div>
          </div>
        </div>
      )}
      {products && (
        <div className="container align-items-center justify-content-center text-center Font">
          <div className="row pt-5">
            <div className="col-lg-9 col-12">
              <InputGroup className="mb-3  w-100">
                <Form.Control
                  className=""
                  placeholder={query}
                  aria-label="Text input with dropdown button"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                />
                <IconSearch className="mt-2 ms-2" />
              </InputGroup>
            </div>
            <div className="col-lg-3  col-12">
              <DropdownButton
                title={category}
                id="category"
                onSelect={handleCat}
                align="end"
              >
                <Dropdown.Item eventKey="General">General</Dropdown.Item>
                <Dropdown.Item eventKey="Grocery">Grocery</Dropdown.Item>
                <Dropdown.Item eventKey="Clothes">Clothes</Dropdown.Item>
              </DropdownButton>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-3 col-12"></div>
            <div className="col-lg-6 pt-lg-0 pt-3 col-12">
              <button
                onClick={fetchData}
                type="button"
                className="btn btn-secondary"
              >
                Find My Product!
              </button>
            </div>
            <div className="col-lg-3 col-12"></div>
          </div>
          <div className="row pt-5">
            <div className="col-12">
              <h3 className="border-bottom mb-4 heartbeat">SEARCH RESULTS</h3>
            </div>
          </div>
          <div className="row">
            {products.map((item) => (
              <div className="col-lg-4 mb-3 d-flex align-items-stretch">
                <div className="card bg-dark Font">
                  <img
                    src={item.Img}
                    className="card-img-top"
                    alt={item.Title}
                  />
                  <div className="card-body d-flex flex-column">
                    <h5 className="card-title  product-title-font">{item.Title}</h5>
                    <p className="card-text mb-4 product-price-font">
                      {item.Price} 
                    </p>
                    <a
                      href={item.Link}
                      target="_blank"
                      className="btn btn-primary mt-auto align-self-center"
                      rel="noreferrer"
                    >
                      Check it out
                    </a>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
