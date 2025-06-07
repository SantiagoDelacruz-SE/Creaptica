import { Routes } from '@angular/router';
import { InicioComponent } from './components/inicio/inicio.component'; // 1. Importa el componente de inicio
import { ListaDocumentosComponent } from './components/lista-documentos/lista-documentos.component'; // 2. Importa el componente de la lista

export const routes: Routes = [
    // 3. Define las rutas
    { path: 'inicio', component: InicioComponent },
    { path: 'documentos', component: ListaDocumentosComponent },

    // 4. (Opcional pero recomendado) Redirige la ruta base a '/inicio'
    { path: '', redirectTo: '/inicio', pathMatch: 'full' }
];
