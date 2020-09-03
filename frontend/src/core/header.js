import React from "react";
import {Nav, Container, Navbar } from "react-bootstrap";

export default class Header extends React.Component {
  render() {
    return (
      <Container fluid>
        <Navbar expand="lg" variant="light" bg="light">
          <Nav className="justify-content-center" activeKey="/home">
            <Nav.Item>
              <Nav.Link href="/home">Active</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link-1">Link</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link-2">Link</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="disabled" disabled>
                Disabled
              </Nav.Link>
            </Nav.Item>
          </Nav>
        </Navbar>
      </Container>
    );
  }
}
