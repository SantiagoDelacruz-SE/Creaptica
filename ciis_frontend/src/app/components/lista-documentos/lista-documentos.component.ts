// Ubicación: src/app/components/lista-documentos/lista-documentos.component.ts
import { Component, OnInit } from '@angular/core';
import { Documento, DocumentoService } from '../../services/documento.service';
import { CommonModule } from '@angular/common'; // Para usar *ngFor y *ngIf

@Component({
  selector: 'app-lista-documentos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista-documentos.component.html',
  styleUrls: ['./lista-documentos.component.scss']
})
export class ListaDocumentosComponent implements OnInit {
  documentos: Documento[] = [];
  cargando = true;
  error: string | null = null;

  constructor(private documentoService: DocumentoService) {}

  ngOnInit(): void {
    this.documentoService.getDocumentos().subscribe({
      next: (data) => {
        // Cuando la petición es exitosa
        this.documentos = data;
        this.cargando = false;
      },
      error: (err) => {
        // Cuando hay un error
        console.error('Error al obtener los documentos:', err);
        this.error = 'No se pudieron cargar los documentos. Asegúrate de que el backend de Django esté funcionando.';
        this.cargando = false;
      }
    });
  }
}
