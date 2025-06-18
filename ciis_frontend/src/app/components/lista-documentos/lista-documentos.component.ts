import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DocumentoService } from '../../services/documento.service';
import { AuthService } from '../../services/auth.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-lista-documentos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista-documentos.component.html',
})
export class ListaDocumentosComponent implements OnInit {
  documentos: any[] = [];
  // La variable se llama 'isLoading'
  isLoading = true;
  error: string | null = null;
  userProfile$: Observable<any>;

  constructor(
    private documentoService: DocumentoService,
    private authService: AuthService
  ) {
    this.userProfile$ = this.authService.userProfile$;
  }

  ngOnInit(): void {
  this.documentoService.getDocumentos().subscribe({ // <-- CORREGIDO: getDocuments()
    next: (data) => {
      this.documentos = data;
      this.isLoading = false;
    },
    error: (err) => {
      this.error = 'No se pudieron cargar los documentos. Puede que no tengas permisos.';
      this.isLoading = false;
      console.error(err);
      },
    });
  }
}
