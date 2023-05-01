import React, { useState, useEffect } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import Form from "react-bootstrap/Form";

import InputGroup from "react-bootstrap/InputGroup";
import IconSearch from "./imgs/search";
import Productcard from "./productcard";
import "./css/style.css";
import { Row } from "react-bootstrap";

export default function Home() {
  const [products, setProducts] = useState(null);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("Category");
  const [sorting, setSorting] = useState("Sort");
  const [isUsed, setIsUsed] = useState(false);
  const [numbersOfSites, setNumbersOfSites] = useState(0);

  useEffect(() => {
    const uniqueStores = [];
    try {
      products.forEach((product) => {
        if (!uniqueStores.includes(product.Shop)) {
          uniqueStores.push(product.Shop);
        }
      });
      setNumbersOfSites(uniqueStores.length);
    } catch (error) {
      console.log(error);
    }
  }, [products]);

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
                <Dropdown.Item className="text-resp" eventKey="videogames">
                  Consoles and Videogames
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
                className="btn btn-success"
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
                <Dropdown.Item className="text-resp" eventKey="videogames">
                  Consoles and Videogames
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
                className="btn btn-success"
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
              <p className="align-self-start text-start">
                FOUND {products.length} ITEMS FROM {numbersOfSites} WEBSITES
              </p>
            </div>
          </div>
          <Row xs={1} md={4} className="g-4">
            {products.map((product) => (
              <Productcard product={product} />
            ))}
          </Row>
        </div>
      )}
    </div>
  );
}
