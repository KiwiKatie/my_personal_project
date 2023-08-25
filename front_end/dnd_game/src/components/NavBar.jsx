import React from 'react';
import { Container, Navbar, Nav, NavDropdown } from 'react-bootstrap';
import api from './utilities';
import { useNavigate } from 'react-router-dom';

function NavBar() {
    const navigate = useNavigate();
    const handleLogout = async () => {
        const token= localStorage.token;
        const headers = {
            Authorization: `Token ${token}`,
          };
        try {
          let response = await api.post('/user/logout/', { headers});
          localStorage.removeItem("token", response.data);
            api.defaults.headers.common["Authorization"] = `Token ${response.data}`;
            navigate("/");
            window.location.reload(); 
        } catch (error) {
          console.error(error);
        }
      };

  return (
    <Navbar expand="lg" bg="light" className="custom-navbar">
      <Container>
        <Navbar.Brand href="#home">Quest for the Taco Bell</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link onClick={handleLogout}>Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;
