javascript
// patches/PATCH_01/service.js
import { api } from './api';
class Service {
  constructor() {
    this.api = new api();
  }
  doSomething() {
    // code here
  }
}
export default Service;