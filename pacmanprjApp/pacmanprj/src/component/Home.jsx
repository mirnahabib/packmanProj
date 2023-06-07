import React, { useState, useEffect } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import Form from "react-bootstrap/Form";

import InputGroup from "react-bootstrap/InputGroup";
import IconSearch from "./imgs/search";
import Productcard from "./productcard";
import "./css/style.css";
import { Row } from "react-bootstrap";

import Slider from "rc-slider";
import "rc-slider/assets/index.css";

const categories = {
  clothingMen: "Clothing and Fashion (Men)",
  clothingWomen: "Clothing and Fashion (Women)",
  clothingKids: "Clothing and Fashion (Kids)",
  cosmetics: "Cosmetics and Bodycare",
  electronics: "Electronics and Devices",
  furniture: "Furnitures and Decor",
  grocery: "Groceries and Supplies",
  toys: "Toys and Games",
  videogames: "Consoles and Videogames",
  computerhardware: "Computer Hardware",
  supplements: "Vitamins and Supplements",
  circuits: "Circuits and Components",
  other: "Other (longer search)",
};
export default function Home() {
  const [products, setProducts] = useState(null);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("Category");
  const [sorting, setSorting] = useState("Sort");
  const [isUsed, setIsUsed] = useState(false);
  const [numbersOfSites, setNumbersOfSites] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [maxPrice, setmaxPrice] = useState(999999);
  const [minPrice, setminPrice] = useState(0);
  const [priceRange, setPriceRange] = useState([minPrice, maxPrice]);
  const [Stores, setStores] = useState(["All"]);
  const [selectedStore, setSelectedStore] = useState("All");

  useEffect(() => {
    const uniqueStores = [];
    try {
      filteredProducts.forEach((product) => {
        if (!uniqueStores.includes(product.Shop)) {
          uniqueStores.push(product.Shop);
        }
      });
      setNumbersOfSites(uniqueStores.length);
    } catch (error) {
      console.log(error);
    }
  }, [filteredProducts]);

  useEffect(() => {
    const uniqueStores = [];
    try {
      products.forEach((product) => {
        if (!uniqueStores.includes(product.Shop)) {
          uniqueStores.push(product.Shop);
        }
      });
      setStores([["All"], ...uniqueStores]);
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

  const handleSelectedStore = (e) => {
    setSelectedStore(e);
  };

  const fetchData = async () => {
    setIsLoading(true);
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
    setIsLoading(false);
  };

  const handleUsed = () => {
    setIsUsed(!isUsed);
  };

  useEffect(() => {
    if (products) {
      let max = 0;
      let min = 1000000000000000;

      products.forEach((product) => {
        if (product.Price > max) {
          max = product.Price;
          setmaxPrice(product.Price);
        }
        if (product.Price < min) {
          min = product.Price;
          setminPrice(product.Price);
        }
      });
    }
  }, [products]);

  useEffect(() => {
    if (products) {
      setFilteredProducts(products);
    }
  }, [products]);

  const handlePriceChange = (value) => {
    setPriceRange(value);
  };

  function filter() {
    if (products) {
      if (selectedStore !== "All") {
        setFilteredProducts(
          products.filter(
            (product) =>
              product.Price >= priceRange[0] &&
              product.Price <= priceRange[1] &&
              product.Shop === selectedStore
          )
        );
      } else {
        setFilteredProducts(
          products.filter(
            (product) =>
              product.Price >= priceRange[0] && product.Price <= priceRange[1]
          )
        );
      }
    }
  }

  return (
    <div className="">
      {!products && (
        //container align-items-center justify-content-center text-center Font
        <div className="row position-absolute top-50 start-50 translate-middle Font align-items-center justify-content-center text-center col-lg-8">
          {/* <Image src={logo} fluid /> */}
          <div className="row heartbeat">
            <div className="col-12 ">
              <h3 className="pb-3 mt-3  ">Find what you are looking for</h3>
            </div>
          </div>
          <div className="row">
            <InputGroup className="mb-3">
              <div className="col">
                <Form.Control
                  className=""
                  placeholder="Search..."
                  aria-label="Text input with dropdown button"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                />
              </div>
              <div className="col-md-auto">
                <IconSearch className="mt-2 ms-2" />
              </div>
              <div className="col-12 col-md-auto">
                <button
                  onClick={() => {
                    if (category !== "Category") {
                      fetchData();
                    }
                  }}
                  type="button"
                  className="btn btn-success ms-2"
                >
                  Find My Product!
                </button>
              </div>
              {isLoading && (
                <div className="d-flex align-items-center ms-2">
                  <div
                    className="spinner-border text-success me-2"
                    role="status"
                  >
                    <span className="visually-hidden">Loading...</span>
                  </div>
                </div>
              )}
            </InputGroup>
          </div>
          <div className="row">
            <div className="col-md-auto">
              <DropdownButton
                title={category}
                id="category"
                onSelect={handleCat}
                align="end"
              >
                {Object.keys(categories).map((cat) => (
                  <Dropdown.Item key={cat} className="text-resp" eventKey={cat}>
                    {categories[cat]}
                  </Dropdown.Item>
                ))}
              </DropdownButton>
            </div>
            <div className="col">
              <div className="d-inline">
                <input type="checkbox" checked={isUsed} onChange={handleUsed} />
              </div>
              <div className="d-inline ps-3">
                look for secondhand products as well
              </div>
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
            <div className="col-lg-3 col-md-auto">
              <button
                onClick={fetchData}
                type="button"
                className="btn btn-success"
              >
                Find My Product!
              </button>
              {isLoading && (
                <div className="d-flex align-items-center ms-2 col-md-auto">
                  <div
                    className="spinner-border text-success me-2"
                    role="status"
                  >
                    <span className="visually-hidden">Loading...</span>
                  </div>
                </div>
              )}
            </div>
          </div>
          <div className="row">
            <div className="col-md-auto">
              <DropdownButton
                title={category}
                id="category"
                onSelect={handleCat}
                align="end"
              >
                {Object.keys(categories).map((cat) => (
                  <Dropdown.Item key={cat} className="text-resp" eventKey={cat}>
                    {categories[cat]}
                  </Dropdown.Item>
                ))}
              </DropdownButton>
            </div>
            <div className="col">
              <div className="d-inline">
                <input type="checkbox" checked={isUsed} onChange={handleUsed} />
              </div>
              <div className="d-inline">
                look for secondhand products as well
              </div>
            </div>
          </div>


          <div className="row pt-3 justify-content-center">
            <div class="filter">
              <div class="filter" style={{position: "absolute",top: 100,right: 5,width: "15%",height: "100vh"}}>
            <br />
                <p>Price Range</p>
                <Slider
                  min={minPrice}
                  max={maxPrice}
                  range
                  defaultValue={[minPrice, maxPrice]}
                  value={priceRange}
                  onChange={handlePriceChange}
                />
                <div >
                  {/* <span>{`${priceRange} EGP `}</span> */}
                  <span>[{priceRange[0]}-{priceRange[1]}] EGP</span>
                </div>
                <div className="row">
                  <div className="col" >
                  <br/>
                  <p>Website:</p>
                    <DropdownButton
                      title={selectedStore}
                      id="store"
                      onSelect={handleSelectedStore}
                      align="end"
                    >
                      {Stores.map((store) => (
                        <Dropdown.Item className="text-resp" eventKey={store}>
                          {store}
                        </Dropdown.Item>
                      ))}
                    </DropdownButton>
                  </div>
                </div>
                <button className="btn btn-success mt-3" onClick={filter}>
                  filter
                </button>
                <br/>
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
            </div>
          </div>




          <div className="row pt-5">
            <div className="col-12">
              <h3 className="border-bottom mb-4 heartbeat">SEARCH RESULTS</h3>

              <p className="align-self-start text-start">
                FOUND {filteredProducts.length} ITEMS FROM {numbersOfSites}{" "}
                WEBSITES
              </p>
            </div>
          </div>
          <Row sm={1} md={3} lg={4} className="g-4">
            {filteredProducts.map((product) => (
              <Productcard product={product} />
            ))}
          </Row>
        </div>
      )}
    </div>
  );
}
