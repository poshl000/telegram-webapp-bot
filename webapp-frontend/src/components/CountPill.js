import { Container, Row, Col, Badge } from 'react-bootstrap';

export default function CountPill({ product, id }){
    return (
        <Container className='d-flex justify-content-end seed-card-pill'>
                <Row>
                  <Col>
                    {product.count > 0 && <Badge pill bg="primary">{product.count}</Badge>}
                  </Col>
                </Row>
        </Container>
    );
}