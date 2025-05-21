import express from 'express'; 
import mapRoutes from './routes'; 

const app = express();
const PORT = 1245; 
const HOST = 'localhost'; 

mapRoutes(app); 
app.listen(PORT, () => {
  console.log(`Server listening at http://${HOST}:${PORT}`); 
});

export default app; 
module.exports = app;