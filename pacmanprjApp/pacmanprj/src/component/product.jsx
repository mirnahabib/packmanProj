import React, { useState, useEffect } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import Form from "react-bootstrap/Form";
import IconAmazon from "./imgs/amazon";
import InputGroup from "react-bootstrap/InputGroup";
import IconSearch from "./imgs/search";
import "./css/style.css";
import amazon from "./imgs/amazon.svg";

export default function Product() {
  const [products, setProducts] = useState(null);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("Category");
  const [sorting, setSorting] = useState("Sort");
  const [isUsed, setIsUsed] = useState(false);

  useEffect(() => {
    let sortProducts;
    if (sorting === "A-Z") {
      sortProducts = [...products].sort((a, b) => {
        return a.Title > b.Tittle ? 1 : -1;
      });
    } else if (sorting === "Z-A") {
      sortProducts = [...products].sort((a, b) => {
        return a.Title > b.Title ? -1 : 1;
      });
    } else if (sorting === "Price ↑") {
      sortProducts = [...products].sort((a, b) => {
        return a.Price > b.Price ? 1 : -1;
      });
    } else if (sorting === "Price ↓") {
      sortProducts = [...products].sort((a, b) => {
        return a.Price > b.Price ? -1 : 1;
      });
    }
    setProducts(sortProducts);
  }, [sorting]);

  const handleSorting = (e) => {
    setSorting(e);
  };

  const handleCat = (e) => {
    setCategory(e);
  };

  const fetchData = async () => {
    let response;
    try {
      if (isUsed === false)
        response = await fetch(`/api/search/${category}/${query}`);
      else if (isUsed === true)
        response = await fetch(`/api/search/used/${category}/${query}`);

      const jsonData = await response.json();
      setProducts(jsonData.jsonresult);
    } catch (error) {
      console.error(error);
    }
    console.log(products);
    console.log(`${query} ${category}`);
  };

  const handleUsed = () => {
    setIsUsed(!isUsed);
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
                <Dropdown.Item className="text-resp" eventKey="clothingMen">
                  Clothing and Fashion (Men)
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="clothingWomen">
                  Clothing and Fashion (Women)
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="cosmetics">
                  Cosmetics and Bodycare
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="electronics">
                  Electronics and Devices
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="furniture">
                  Furnitures and Decor
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="grocery">
                  Groceries and Supplies
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="toys">
                  Toys and Games
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="other">
                  Other (longer search)
                </Dropdown.Item>
              </DropdownButton>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-3 col-12"></div>
            <div className="col-lg-6 pt-lg-0 pt-3 col-12 ">
              <button
                onClick={fetchData}
                type="button"
                className="btn btn-secondary"
              >
                Find My Product!
              </button>
            </div>
            <div className="col-lg-3 col-12 pt-2 pe-5 ">
              <div className="d-inline">
                <input type="checkbox" checked={isUsed} onChange={handleUsed} />
              </div>
              <div className="d-inline ps-3">look for secondhand</div>
            </div>
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
                <Dropdown.Item className="text-resp" eventKey="clothingMen">
                  Clothing and Fashion (Men)
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="clothingWomen">
                  Clothing and Fashion (Women)
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="cosmetics">
                  Cosmetics and Bodycare
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="electronics">
                  Electronics and Devices
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="furniture">
                  Furnitures and Decor
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="grocery">
                  Groceries and Supplies
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="toys">
                  Toys and Games
                </Dropdown.Item>
                <Dropdown.Item className="text-resp" eventKey="other">
                  Other (longer search)
                </Dropdown.Item>
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
            <div className="col-lg-3 col-12 pt-2 pe-5 ">
              <div className="d-inline">
                <input type="checkbox" checked={isUsed} onChange={handleUsed} />
              </div>
              <div className="d-inline ps-3">look for secondhand</div>
            </div>
          </div>
          <div className="row pt-3 justify-content-center">
            <DropdownButton
              title={sorting}
              id="sort"
              onSelect={handleSorting}
              align="end"
            >
              <Dropdown.Item eventKey="A-Z">A-Z</Dropdown.Item>
              <Dropdown.Item eventKey="Z-A">Z-A</Dropdown.Item>
              <Dropdown.Item eventKey="Price ↑">Price ↑</Dropdown.Item>
              <Dropdown.Item eventKey="Price ↓">Price ↓</Dropdown.Item>
            </DropdownButton>
          </div>
          <div className="row pt-5">
            <div className="col-12">
              <h3 className="border-bottom mb-4 heartbeat">SEARCH RESULTS</h3>
            </div>
          </div>
          <div className="row">
            {sorting &&
              products.map((item) => (
                <div className="col-lg-4 mb-3 d-flex align-items-stretch">
                  <div className="card bg-dark w-100 Font">
                    <img
                      src={item.Img}
                      className="card-img-top img-props"
                      alt={item.Title}
                    />
                    <div className="card-body d-flex flex-column">
                      <h5 className="card-title  product-title-font text-light">
                        {item.Title}
                      </h5>
                      {item.Price !== 0 ? (
                        <p className="card-text mb-4 product-price-font">
                          {item.Price} EGP
                        </p>
                      ) : (
                        <p className="card-text mb-4 product-price-font">
                          price unavailable
                        </p>
                      )}

                      <a
                        href={item.Link}
                        target="_blank"
                        className="btn btn-primary mt-auto align-self-center"
                        rel="noreferrer"
                      >
                        Check it out
                      </a>
                      {/* {item.Shop === "Amazon" ? 
                      <IconAmazon className="align-self-end"/>: " "
                      } */}
                      <small className="align-self-end shop-name">{item.Shop}</small>
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
