import ProductCard from './components/ProductCard'

import './App.css';
import { Container, Row } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Shop({ addProduct, rmProduct, products }) {
    
    return (
        <Container fluid style={{ padding: '10px' }}>
          <Row xs={2} md={1} className="g-1">

            {products.map((product, id) => 
              <ProductCard id={id} product={product} addProduct={addProduct} rmProduct={rmProduct} />
            )}

          </Row>
        </Container>
    );
}