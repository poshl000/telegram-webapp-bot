import { Card, Container, Row, Col, Badge } from 'react-bootstrap';
import CountPill from './CountPill';


export default function ProductCard({id, product, addProduct, rmProduct}) {
    return (
        <Col>
            <Card className='seed-card'>
                <CountPill product={product} id={id} />
                <Card.Img variant="top" src="https://via.placeholder.com/420.png" />
                <Card.Body>
                    <Card.Title>{product.name}</Card.Title>
                    <Card.Text>
                        <Badge bg="primary">Attribute</Badge> <Badge bg="success">Attribute</Badge> <Badge bg="dark">Attribute</Badge> <Badge bg="warning" text="dark">Attribute</Badge>
                    </Card.Text>
                    <Container className='justify-content-between'>
                        <Row>
                            <Col>
                                {product.count > 0 && <button className="Button" onClick={() => rmProduct(id)}>🗑️</button>}
                            </Col>
                            <Col>
                                <button className="Button" onClick={() => addProduct(id)}>Add</button>
                            </Col>
                        </Row>
                    </Container>
                </Card.Body>
            </Card>
        </Col>
    )
}