import { Routes } from '@angular/router';
import { InicioComponent } from './components/inicio/inicio.component';
import { ListaDocumentosComponent } from './components/lista-documentos/lista-documentos.component';
import { LoginComponent } from './components/auth/login/login.component';

export const routes: Routes = [
    { path: 'inicio', component: InicioComponent },
    { path: 'documentos', component: ListaDocumentosComponent },
    { path: 'login', component: LoginComponent },
    { path: '', redirectTo: '/inicio', pathMatch: 'full' }
];
