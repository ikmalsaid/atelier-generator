<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atelier Generator</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
    <style>
        @font-face {
            font-family: "Nokia Sans S60 Regular";
            src: url("https://db.onlinewebfonts.com/t/91365a119c448bf9da6d8f710e3bdda6.svg#Nokia Sans S60 Regular")format("svg");
        }
        :root {
            --primary: #FF4B91;
            --primary-hover: #FF6BA5;
            --secondary: #2D3250;
            --accent: #424769;
            --background: #1A1B26;
            --surface: #232433;
            --text: #E5E7EB;
            --text-secondary: #9CA3AF;
            --error: #EF4444;
            --success: #10B981;
            --radius: 12px;
            --radius-sm: 8px;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Nokia Sans S60 Regular";
            scrollbar-width: thin;
            scrollbar-color: var(--accent) var(--background);
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--background);
            color: var(--text);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
        }

        .container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 2rem;
            padding: 1rem 0;
            border-bottom: 1px solid var(--accent);
        }

        .header h1 {
            font-size: 1.5rem;
            font-weight: 600;
            background: linear-gradient(to right, var(--primary), #A367B1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header p {
            color: var(--text-secondary);
            font-size: 0.875rem;
        }

        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: 280px;
            height: 100vh;
            background: var(--surface);
            padding: 2rem;
            overflow-y: auto;
            border-right: 1px solid var(--accent);
        }

        .main-content {
            margin-left: 280px;
            padding: 2rem;
        }

        .nav-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            margin-bottom: 0.5rem;
            color: var(--text);
            text-decoration: none;
            border-radius: var(--radius-sm);
            transition: all 0.2s;
            cursor: pointer;
            font-size: 0.875rem;
        }

        .nav-item i {
            width: 1.25rem;
            text-align: center;
            font-size: 1rem;
        }

        .nav-item:hover {
            background: var(--accent);
        }

        .nav-item.active {
            background: var(--primary);
            color: white;
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.3s ease-in-out;
        }

        .tab-content.active {
            display: block;
        }

        .card {
            background: var(--surface);
            border-radius: var(--radius);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.875rem;
        }

        .form-control {
            width: 100%;
            padding: 0.75rem 1rem;
            background: var(--background);
            border: 1px solid var(--accent);
            border-radius: var(--radius-sm);
            color: var(--text);
            font-size: 0.875rem;
            transition: all 0.2s;
        }

        select.form-control {
            appearance: none;
            -webkit-appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12' fill='none'%3E%3Cpath d='M2.5 4.5L6 8L9.5 4.5' stroke='%239CA3AF' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 1rem center;
            padding-right: 2.5rem;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(255, 75, 145, 0.1);
        }

        textarea.form-control {
            min-height: 100px;
            resize: vertical;
        }

        .toolkit-btn {
            justify-content: normal !important;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.75rem 1.5rem;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: var(--radius-sm);
            font-size: 0.875rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
            position: relative;
            width: 100%;
            min-height: 2.75rem;
            gap: 0.5rem;
        }

        .btn:hover {
            background: var(--primary-hover);
        }

        .btn:disabled {
            opacity: 0.7;
            cursor: not-allowed;
        }

        .btn-secondary {
            background: var(--accent);
        }

        .btn-secondary:hover {
            background: var(--secondary);
        }

        .gallery {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .gallery-row {
            border-bottom: 1px solid var(--accent);
            padding-bottom: 1.5rem;
        }

        .gallery-row:last-child {
            border-bottom: none;
        }

        .gallery-row-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
            padding: 0.5rem;
            background: var(--background);
            border-radius: var(--radius-sm);
        }

        .gallery-row-title {
            font-size: 0.875rem;
            color: var(--text-secondary);
            margin-right: 1rem;
            flex: 1;
            word-break: break-word;
        }

        .gallery-row-copy {
            background: var(--accent);
            color: var(--text);
            border: none;
            border-radius: var(--radius-sm);
            padding: 0.25rem 0.5rem;
            cursor: pointer;
            font-size: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.25rem;
            transition: all 0.2s;
        }

        .gallery-row-copy:hover {
            background: var(--primary);
        }

        .gallery-row-images {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
            padding: 0.5rem;
        }

        .gallery-item {
            position: relative;
            border-radius: var(--radius);
            overflow: hidden;
            aspect-ratio: 1;
            cursor: pointer;
            transition: all 0.2s;
        }

        .gallery-item:hover {
            transform: scale(1.02);
            box-shadow: var(--shadow);
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.2s;
        }

        .gallery-item .actions {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            opacity: 0;
            transition: opacity 0.2s;
        }

        .gallery-item:hover .actions {
            opacity: 1;
        }

        .gallery-item .action-btn {
            background: var(--surface);
            color: var(--text);
            border: none;
            border-radius: var(--radius-sm);
            padding: 0.5rem;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            font-size: 1rem;
        }

        .gallery-item .action-btn:hover {
            background: var(--primary);
            transform: scale(1.1);
        }

        .dropzone {
            border: 2px dashed var(--accent);
            border-radius: var(--radius);
            padding: 2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
            background: var(--background);
            min-height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
        }

        .dropzone:hover {
            border-color: var(--primary);
        }

        .dropzone.dragover {
            border-color: var(--primary);
            background: rgba(255, 75, 145, 0.05);
        }

        .dropzone-content {
            color: var(--text-secondary);
            font-size: 0.875rem;
        }

        .loading {
            position: relative;
        }

        .loading::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.875rem;
            color: var(--text);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                height: auto;
                position: relative;
                padding: 1rem;
            }

            .main-content {
                margin-left: 0;
                padding: 1rem;
            }

            .container {
                padding: 1rem;
            }

            .gallery-row-images {
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            }
        }

        .checkbox-wrapper {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .checkbox-wrapper input[type="checkbox"] {
            appearance: none;
            -webkit-appearance: none;
            width: 1.2rem;
            height: 1.2rem;
            border: 2px solid var(--accent);
            border-radius: var(--radius-sm);
            background: var(--background);
            cursor: pointer;
            position: relative;
            transition: all 0.2s;
            vertical-align: top;
        }

        .checkbox-wrapper input[type="checkbox"]:checked {
            background: var(--primary);
            border-color: var(--primary);
        }

        .checkbox-wrapper input[type="checkbox"]:checked::after {
            content: '✓';
            color: white;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 0.8rem;
        }

        .checkbox-wrapper input[type="checkbox"]:hover {
            border-color: var(--primary);
        }

        .checkbox-wrapper label {
            color: var(--text);
            font-size: 0.875rem;
            cursor: pointer;
        }

        .button-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .range {
            -webkit-appearance: none;
            width: 100%;
            height: 6px;
            background: var(--accent);
            border-radius: 3px;
            outline: none;
            padding: 0;
            margin: 0;
        }

        .range::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: var(--primary);
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }

        .range::-webkit-slider-thumb:hover {
            background: var(--primary-hover);
            transform: scale(1.2);
        }

        .range-value {
            color: var(--text-secondary);
            font-size: 0.875rem;
            margin-top: 0.5rem;
            text-align: right;
        }

        .text-results {
            margin-top: 2rem;
            border-top: 1px solid var(--accent);
            padding-top: 2rem;
        }

        .range::-moz-range-thumb {
            width: 16px;
            height: 16px;
            border: 0;
            border-radius: 50%;
            background: var(--primary);
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }

        .range::-moz-range-thumb:hover {
            background: var(--primary-hover);
            transform: scale(1.2);
        }

        .range::-moz-range-track {
            width: 100%;
            height: 6px;
            background: var(--accent);
            border-radius: 3px;
            border: none;
        }

        /* Image Toolkit specific styles */
        .toolkit-container {
            display: grid;
            grid-template-columns: 350px 1fr;
            gap: 1.5rem;
            align-items: start;
        }

        .toolkit-sidebar {
            position: sticky;
            top: 1rem;
        }

        .toolkit-actions {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--accent);
        }

        .toolkit-main {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .toolkit-results {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        @media (max-width: 1200px) {
            .toolkit-container {
                grid-template-columns: 1fr;
            }
            
            .toolkit-actions {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 640px) {
            .toolkit-actions {
                grid-template-columns: 1fr;
            }
        }

        /* Page Layout Styles */
        .page-container {
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 1.5rem;
            align-items: start;
        }

        .page-sidebar {
            position: sticky;
            top: 1rem;
        }

        .page-main {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .page-actions {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }

        .page-results {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        @media (max-width: 1200px) {
            .page-container {
                grid-template-columns: 1fr;
                max-width: 800px;
                margin: 0 auto;
            }

            .page-sidebar {
                position: relative;
                top: 0;
            }
        }

        @media (max-width: 768px) {
            .form-group {
                margin-bottom: 1rem;
            }

            .gallery {
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            }
        }

        /* Specific page styles */
        .rt-actions {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
        }

        .canvas-tools {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
        }

        .outpaint-controls {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }

        /* Empty state styles */
        .gallery:empty {
            min-height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--surface);
            border-radius: var(--radius);
            color: var(--text-secondary);
            font-size: 0.875rem;
        }

        .gallery:empty::after {
            content: 'No images generated yet';
        }

        .text-results:empty {
            display: none;
        }

        /* Modal styles */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.85);
            z-index: 1000;
            padding: 2rem;
            overflow-y: auto;
            backdrop-filter: blur(8px);
        }

        .modal.active {
            display: flex;
            animation: fadeIn 0.3s ease-in-out;
        }

        .modal-content {
            position: relative;
            margin: auto;
            max-width: 90%;
            max-height: 90vh;
            background: var(--surface);
            border-radius: var(--radius);
            padding: 1.5rem;
            box-shadow: var(--shadow);
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .modal-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--accent);
        }

        .modal-title {
            font-size: 1.125rem;
            color: var(--text);
            font-weight: 500;
        }

        .modal-close {
            position: relative;
            top: 0;
            right: 0;
            background: var(--accent);
            color: var(--text);
            border: none;
            border-radius: var(--radius-sm);
            width: 32px;
            height: 32px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            z-index: 1;
        }

        .modal-close:hover {
            background: var(--primary);
            transform: scale(1.1);
        }

        .modal-body {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 200px;
            overflow: hidden;
        }

        .modal-image {
            max-width: 100%;
            max-height: calc(90vh - 12rem);
            object-fit: contain;
            border-radius: var(--radius);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }

        .modal-actions {
            display: flex;
            justify-content: flex-end;
            gap: 1rem;
            padding-top: 1rem;
            border-top: 1px solid var(--accent);
        }

        .modal-btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: var(--radius-sm);
            background: var(--accent);
            color: var(--text);
            cursor: pointer;
            font-size: 0.875rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
        }

        .modal-btn:hover {
            background: var(--primary);
        }

        .modal-btn i {
            font-size: 1rem;
        }

        /* Footer styles */
        .footer {
            margin-top: 3rem;
            padding: 2rem;
            text-align: center;
            border-top: 1px solid var(--accent);
            color: var(--text-secondary);
            font-size: 0.875rem;
            line-height: 1.6;
        }

        /* Loading spinner */
        .btn.loading {
            color: transparent;
            pointer-events: none;
        }

        .btn.loading::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 50%;
            width: 1.25rem;
            height: 1.25rem;
            margin: -0.625rem 0 0 -0.625rem;
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-top-color: white;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            box-sizing: border-box;
        }

        .btn span {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn.loading span {
            visibility: hidden;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Error popup */
        .error-popup {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--error);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            z-index: 1000;
            max-width: 400px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            animation: slideIn 0.3s ease-out;
            font-size: 0.875rem;
        }

        .error-popup .close {
            background: none;
            border: none;
            color: white;
            cursor: pointer;
            padding: 0.25rem;
            font-size: 1.25rem;
            opacity: 0.8;
            transition: opacity 0.2s;
        }

        .error-popup .close:hover {
            opacity: 1;
        }

        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        @media (max-width: 768px) {
            .error-popup {
                bottom: 1rem;
                right: 1rem;
                left: 1rem;
                max-width: none;
            }
        }

        /* Sidebar copyright */
        .sidebar-footer {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid var(--accent);
            color: var(--text-secondary);
            font-size: 0.75rem;
            line-height: 1.6;
            text-align: center;
        }

        .sidebar-footer p {
            margin-bottom: 0.5rem;
        }

        .sidebar {
            display: flex;
            flex-direction: column;
            height: 100vh;
        }

        .sidebar nav {
            flex: 1;
            overflow-y: auto;
            margin-bottom: 1rem;
        }

        .api-section table {
            font-size: 0.875rem;
        }

        .api-section td {
            padding: 0.75rem;
            border-bottom: 1px solid var(--accent);
            vertical-align: top;
        }

        .api-section td:first-child {
            font-family: monospace;
            white-space: nowrap;
        }

        .api-section ul {
            margin: 0;
            padding-left: 1.25rem;
        }

        .api-section code {
            background: var(--background);
            padding: 0.125rem 0.25rem;
            border-radius: 4px;
            font-size: 0.8125rem;
            font-family: monospace;
        }

        .api-section td:nth-child(2) {
            min-width: 200px;
        }

        .api-docs-container {
            grid-template-columns: auto !important;
        }
    </style>
</head>
<body>
    <div id="unsaved-warning" style="display: none; position: fixed; top: 0; left: 0; right: 0; background: var(--error); color: white; text-align: center; padding: 0.5rem; z-index: 1000;">
        Warning: All unsaved changes will be lost if you refresh or close this page.
    </div>
    <div class="sidebar">
        <div class="header">
            <h1>Atelier Generator</h1>
            <p>v2.0</p>
        </div>
        <nav>
            <a class="nav-item active" data-tab="image-generator">
                <i class="fas fa-palette"></i>
                <span>Image Generator</span>
            </a>
            <a class="nav-item" data-tab="transparent-generator">
                <i class="fas fa-star"></i>
                <span>Transparent Generator</span>
            </a>
            <a class="nav-item" data-tab="image-variation">
                <i class="fas fa-sync-alt"></i>
                <span>Image Variation</span>
            </a>
            <a class="nav-item" data-tab="image-structure">
                <i class="fas fa-cubes"></i>
                <span>Image Structure</span>
            </a>
            <a class="nav-item" data-tab="image-facial">
                <i class="fas fa-user"></i>
                <span>Image Facial</span>
            </a>
            <a class="nav-item" data-tab="image-style">
                <i class="fas fa-paint-brush"></i>
                <span>Image Style</span>
            </a>
            <a class="nav-item" data-tab="image-controlnet">
                <i class="fas fa-gamepad"></i>
                <span>Image Controlnet</span>
            </a>
            <a class="nav-item" data-tab="image-toolkit">
                <i class="fas fa-tools"></i>
                <span>Image Toolkit</span>
            </a>
            <a class="nav-item" data-tab="image-enhance">
                <i class="fas fa-magic"></i>
                <span>Image Enhance</span>
            </a>
            <a class="nav-item" data-tab="object-eraser">
                <i class="fas fa-eraser"></i>
                <span>Object Eraser</span>
            </a>
            <a class="nav-item" data-tab="generative-fill">
                <i class="fas fa-fill-drip"></i>
                <span>Generative Fill</span>
            </a>
            <a class="nav-item" data-tab="rt-generator">
                <i class="fas fa-bolt"></i>
                <span>RT Generator</span>
            </a>
            <a class="nav-item" data-tab="rt-canvas">
                <i class="fas fa-paint-roller"></i>
                <span>RT Canvas</span>
            </a>
            <a class="nav-item" data-tab="image-outpaint">
                <i class="fas fa-expand"></i>
                <span>Image Outpaint</span>
            </a>
            <a class="nav-item" data-tab="api-docs">
                <i class="fas fa-book"></i>
                <span>API Documentation</span>
            </a>
        </nav>
        <div class="sidebar-footer">
            <p>Copyright © 2025 Ikmal Said. All rights reserved.</p>
            <p>AtelierGenerator can make mistakes. Check important info.</p>
        </div>
    </div>

    <main class="main-content">
        <!-- Image Generator -->
        <div id="image-generator" class="tab-content active">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-generator-form">
                            <div class="form-group">
                                <label for="prompt">Prompt</label>
                                <textarea class="form-control" id="prompt" name="prompt" required 
                                    placeholder="Describe what you want to generate..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="model_name">Model</label>
                                <select class="form-control" id="model_name" name="model_name"></select>
                            </div>
                            <div class="form-group">
                                <label for="image_size">Size</label>
                                <select class="form-control" id="image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="lora_svi">SVI LoRA</label>
                                <select class="form-control" id="lora_svi" name="lora_svi"></select>
                            </div>
                            <div class="form-group">
                                <label for="lora_flux">Flux LoRA</label>
                                <select class="form-control" id="lora_flux" name="lora_flux"></select>
                            </div>
                            <div class="form-group">
                                <label for="image_seed">Seed</label>
                                <input type="number" class="form-control" id="image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="style_name">Style</label>
                                <select class="form-control" id="style_name" name="style_name"></select>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="enhance_prompt">
                                    <span>Enhance Prompt</span>
                                </label>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-generator-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Transparent Generator -->
        <div id="transparent-generator" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="transparent-generator-form">
                            <div class="form-group">
                                <label for="trans_prompt">Prompt</label>
                                <textarea class="form-control" id="trans_prompt" name="prompt" required
                                    placeholder="Describe what you want to generate..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="trans_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="trans_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="trans_image_size">Size</label>
                                <select class="form-control" id="trans_image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="trans_image_seed">Seed</label>
                                <input type="number" class="form-control" id="trans_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="trans_style_name">Style</label>
                                <select class="form-control" id="trans_style_name" name="style_name"></select>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="enhance_prompt">
                                    <span>Enhance Prompt</span>
                                </label>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="transparent" checked>
                                    <span>Transparent Background</span>
                                </label>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="transparent-generator-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Variation -->
        <div id="image-variation" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-variation-form">
                            <div class="form-group">
                                <label for="var_image">Source Image</label>
                                <div class="dropzone" id="var_image_dropzone">
                                    <input type="file" id="var_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="var_prompt">Prompt</label>
                                <textarea class="form-control" id="var_prompt" name="prompt" required
                                    placeholder="Describe how you want to vary the image..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="var_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="var_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="var_model_name">Model</label>
                                <select class="form-control" id="var_model_name" name="model_name"></select>
                            </div>
                            <div class="form-group">
                                <label for="var_image_size">Size</label>
                                <select class="form-control" id="var_image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="var_strength">Guide Strength</label>
                                <select class="form-control" id="var_strength" name="strength"></select>
                            </div>
                            <div class="form-group">
                                <label for="var_lora_svi">SVI LoRA</label>
                                <select class="form-control" id="var_lora_svi" name="lora_svi"></select>
                            </div>
                            <div class="form-group">
                                <label for="var_lora_flux">Flux LoRA</label>
                                <select class="form-control" id="var_lora_flux" name="lora_flux"></select>
                            </div>
                            <div class="form-group">
                                <label for="var_image_seed">Seed</label>
                                <input type="number" class="form-control" id="var_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="var_style_name">Style</label>
                                <select class="form-control" id="var_style_name" name="style_name"></select>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="enhance_prompt">
                                    <span>Enhance Prompt</span>
                                </label>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-variation-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Structure -->
        <div id="image-structure" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-structure-form">
                            <div class="form-group">
                                <label for="str_image">Source Image</label>
                                <div class="dropzone" id="str_image_dropzone">
                                    <input type="file" id="str_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="str_prompt">Prompt</label>
                                <textarea class="form-control" id="str_prompt" name="prompt" required
                                    placeholder="Describe the structural changes you want..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="str_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="str_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="str_model_name">Model</label>
                                <select class="form-control" id="str_model_name" name="model_name"></select>
                            </div>
                            <div class="form-group">
                                <label for="str_image_size">Size</label>
                                <select class="form-control" id="str_image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="str_strength">Guide Strength</label>
                                <select class="form-control" id="str_strength" name="strength"></select>
                            </div>
                            <div class="form-group">
                                <label for="str_lora_svi">SVI LoRA</label>
                                <select class="form-control" id="str_lora_svi" name="lora_svi"></select>
                            </div>
                            <div class="form-group">
                                <label for="str_image_seed">Seed</label>
                                <input type="number" class="form-control" id="str_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="str_style_name">Style</label>
                                <select class="form-control" id="str_style_name" name="style_name"></select>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="enhance_prompt">
                                    <span>Enhance Prompt</span>
                                </label>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-structure-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Facial -->
        <div id="image-facial" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-facial-form">
                            <div class="form-group">
                                <label for="fac_image">Source Image</label>
                                <div class="dropzone" id="fac_image_dropzone">
                                    <input type="file" id="fac_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="fac_prompt">Prompt</label>
                                <textarea class="form-control" id="fac_prompt" name="prompt" required
                                    placeholder="Describe the facial changes you want..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="fac_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="fac_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="fac_model_name">Model</label>
                                <select class="form-control" id="fac_model_name" name="model_name"></select>
                            </div>
                            <div class="form-group">
                                <label for="fac_image_size">Size</label>
                                <select class="form-control" id="fac_image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="fac_strength">Guide Strength</label>
                                <select class="form-control" id="fac_strength" name="strength"></select>
                            </div>
                            <div class="form-group">
                                <label for="fac_lora_svi">SVI LoRA</label>
                                <select class="form-control" id="fac_lora_svi" name="lora_svi"></select>
                            </div>
                            <div class="form-group">
                                <label for="fac_image_seed">Seed</label>
                                <input type="number" class="form-control" id="fac_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="fac_style_name">Style</label>
                                <select class="form-control" id="fac_style_name" name="style_name"></select>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="enhance_prompt">
                                    <span>Enhance Prompt</span>
                                </label>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-facial-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Style -->
        <div id="image-style" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-style-form">
                            <div class="form-group">
                                <label for="sty_image">Source Image</label>
                                <div class="dropzone" id="sty_image_dropzone">
                                    <input type="file" id="sty_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="sty_prompt">Prompt</label>
                                <textarea class="form-control" id="sty_prompt" name="prompt" required
                                    placeholder="Describe the style changes you want..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="sty_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="sty_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="sty_model_name">Model</label>
                                <select class="form-control" id="sty_model_name" name="model_name"></select>
                            </div>
                            <div class="form-group">
                                <label for="sty_image_size">Size</label>
                                <select class="form-control" id="sty_image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="sty_strength">Guide Strength</label>
                                <select class="form-control" id="sty_strength" name="strength"></select>
                            </div>
                            <div class="form-group">
                                <label for="sty_lora_svi">SVI LoRA</label>
                                <select class="form-control" id="sty_lora_svi" name="lora_svi"></select>
                            </div>
                            <div class="form-group">
                                <label for="sty_image_seed">Seed</label>
                                <input type="number" class="form-control" id="sty_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="sty_style_name">Style</label>
                                <select class="form-control" id="sty_style_name" name="style_name"></select>
                            </div>
                            <div class="form-group">
                                <label class="checkbox-wrapper">
                                    <input type="checkbox" name="enhance_prompt">
                                    <span>Enhance Prompt</span>
                                </label>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-style-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Controlnet -->
        <div id="image-controlnet" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-controlnet-form">
                            <div class="form-group">
                                <label for="cn_image">Source Image</label>
                                <div class="dropzone" id="cn_image_dropzone">
                                    <input type="file" id="cn_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="cn_prompt">Prompt</label>
                                <textarea class="form-control" id="cn_prompt" name="prompt" required
                                    placeholder="Describe what you want to generate..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="cn_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="cn_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="cn_model_name">Model</label>
                                <select class="form-control" id="cn_model_name" name="model_name"></select>
                            </div>
                            <div class="form-group">
                                <label for="cn_controlnet">Control Type</label>
                                <select class="form-control" id="cn_controlnet" name="controlnet"></select>
                            </div>
                            <div class="form-group">
                                <label for="cn_strength">Control Strength</label>
                                <input type="range" class="form-control range" id="cn_strength" name="strength" 
                                    value="70" min="0" max="100" step="1">
                                <div class="range-value">70%</div>
                            </div>
                            <div class="form-group">
                                <label for="cn_cfg">Prompt Scale</label>
                                <input type="range" class="form-control range" id="cn_cfg" name="cfg" 
                                    value="9.0" min="1" max="20" step="0.1">
                                <div class="range-value">9.0</div>
                            </div>
                            <div class="form-group">
                                <label for="cn_image_seed">Seed</label>
                                <input type="number" class="form-control" id="cn_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="cn_style_name">Style</label>
                                <select class="form-control" id="cn_style_name" name="style_name"></select>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-controlnet-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Toolkit -->
        <div id="image-toolkit" class="tab-content">
            <div class="toolkit-container">
                <div class="toolkit-sidebar">
                    <div class="card">
                        <form id="image-toolkit-form">
                            <div class="form-group">
                                <label for="tk_image">Source Image</label>
                                <div class="dropzone" id="tk_image_dropzone">
                                    <input type="file" id="tk_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="tk_gfpgan_version">GFPGAN Model Version</label>
                                <select class="form-control" id="tk_gfpgan_version" name="model_version">
                                </select>
                            </div>
                        </form>

                        <div class="toolkit-actions">
                            <button type="button" class="btn toolkit-btn" id="tk_gfpgan">
                                <i class="fas fa-sync-alt"></i>
                                <span>Restore Face (GFPGAN)</span>
                            </button>
                            <button type="button" class="btn toolkit-btn" id="tk_codeformer">
                                <i class="fas fa-user-circle"></i>
                                <span>Restore Face (CodeFormer)</span>
                            </button>
                            <button type="button" class="btn toolkit-btn" id="tk_upscale">
                                <i class="fas fa-expand-arrows-alt"></i>
                                <span>Upscale Image</span>
                            </button>
                            <button type="button" class="btn toolkit-btn" id="tk_bgremove">
                                <i class="fas fa-cut"></i>
                                <span>Remove Background</span>
                            </button>
                            <button type="button" class="btn toolkit-btn" id="tk_caption">
                                <i class="fas fa-closed-captioning"></i>
                                <span>Generate Caption</span>
                            </button>
                            <button type="button" class="btn toolkit-btn" id="tk_prompt">
                                <i class="fas fa-comment-alt"></i>
                                <span>Generate Prompt</span>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="toolkit-main">
                    <div class="card toolkit-results">
                        <div class="gallery" id="image-toolkit-results"></div>
                        <div class="text-results">
                            <div class="form-group">
                                <label for="tk_caption_result">Generated Caption</label>
                                <textarea class="form-control" id="tk_caption_result" readonly rows="3"></textarea>
                            </div>
                            <div class="form-group">
                                <label for="tk_prompt_result">Generated Prompt</label>
                                <textarea class="form-control" id="tk_prompt_result" readonly rows="3"></textarea>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Enhance -->
        <div id="image-enhance" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-enhance-form">
                            <div class="form-group">
                                <label for="enh_image">Source Image</label>
                                <div class="dropzone" id="enh_image_dropzone">
                                    <input type="file" id="enh_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="enh_prompt">Prompt</label>
                                <textarea class="form-control" id="enh_prompt" name="prompt"
                                    placeholder="Describe how you want to enhance the image..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="enh_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="enh_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="enh_creativity">Creativity Strength</label>
                                <input type="range" class="form-control range" id="enh_creativity" name="creativity" 
                                    value="0.3" min="0.2" max="1.0" step="0.05">
                                <div class="range-value">0.3</div>
                            </div>
                            <div class="form-group">
                                <label for="enh_resemblance">Resemblance Strength</label>
                                <input type="range" class="form-control range" id="enh_resemblance" name="resemblance" 
                                    value="1.0" min="0.0" max="1.0" step="0.05">
                                <div class="range-value">1.0</div>
                            </div>
                            <div class="form-group">
                                <label for="enh_hdr">HDR Strength</label>
                                <input type="range" class="form-control range" id="enh_hdr" name="hdr" 
                                    value="0.0" min="0.0" max="1.0" step="0.05">
                                <div class="range-value">0.0</div>
                            </div>
                            <div class="form-group">
                                <label for="enh_style_name">Style</label>
                                <select class="form-control" id="enh_style_name" name="style_name"></select>
                            </div>
                            <button type="submit" class="btn">Enhance</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-enhance-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Object Eraser -->
        <div id="object-eraser" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="object-eraser-form">
                            <div class="form-group">
                                <label for="er_image">Source Image</label>
                                <div class="dropzone" id="er_image_dropzone">
                                    <input type="file" id="er_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="er_mask">Mask Image</label>
                                <div class="dropzone" id="er_mask_dropzone">
                                    <input type="file" id="er_mask" name="mask" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your mask image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="er_cfg">Prompt Scale</label>
                                <input type="range" class="form-control range" id="er_cfg" name="cfg" 
                                    value="9.0" min="1" max="20" step="0.1">
                                <div class="range-value">9.0</div>
                            </div>
                            <button type="submit" class="btn">Erase Object</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="object-eraser-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Generative Fill -->
        <div id="generative-fill" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="generative-fill-form">
                            <div class="form-group">
                                <label for="gf_image">Source Image</label>
                                <div class="dropzone" id="gf_image_dropzone">
                                    <input type="file" id="gf_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="gf_mask">Mask Image</label>
                                <div class="dropzone" id="gf_mask_dropzone">
                                    <input type="file" id="gf_mask" name="mask" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your mask image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="gf_prompt">Prompt</label>
                                <textarea class="form-control" id="gf_prompt" name="prompt" required
                                    placeholder="Describe what you want to fill in the masked area..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="gf_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="gf_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="gf_style_name">Style</label>
                                <select class="form-control" id="gf_style_name" name="style_name"></select>
                            </div>
                            <button type="submit" class="btn">Fill Area</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="generative-fill-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RT Generator -->
        <div id="rt-generator" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="rt-generator-form">
                            <div class="form-group">
                                <label for="rtg_prompt">Prompt</label>
                                <textarea class="form-control" id="rtg_prompt" name="prompt" required
                                    placeholder="Describe what you want to generate..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="rtg_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="rtg_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="rtg_image_size">Size</label>
                                <select class="form-control" id="rtg_image_size" name="image_size"></select>
                            </div>
                            <div class="form-group">
                                <label for="rtg_lora">LoRA Model</label>
                                <select class="form-control" id="rtg_lora" name="lora_rt"></select>
                            </div>
                            <div class="form-group">
                                <label for="rtg_image_seed">Seed</label>
                                <input type="number" class="form-control" id="rtg_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="rtg_style_name">Style</label>
                                <select class="form-control" id="rtg_style_name" name="style_name"></select>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="rt-generator-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RT Canvas -->
        <div id="rt-canvas" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="rt-canvas-form">
                            <div class="form-group">
                                <label for="rtc_image">Source Image</label>
                                <div class="dropzone" id="rtc_image_dropzone">
                                    <input type="file" id="rtc_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="rtc_prompt">Prompt</label>
                                <textarea class="form-control" id="rtc_prompt" name="prompt" required
                                    placeholder="Describe what you want to generate..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="rtc_negative_prompt">Negative Prompt</label>
                                <textarea class="form-control" id="rtc_negative_prompt" name="negative_prompt"
                                    placeholder="Describe what you want to avoid..."></textarea>
                            </div>
                            <div class="form-group">
                                <label for="rtc_lora">LoRA Model</label>
                                <select class="form-control" id="rtc_lora" name="lora_rt"></select>
                            </div>
                            <div class="form-group">
                                <label for="rtc_strength">Creativity Strength</label>
                                <input type="range" class="form-control range" id="rtc_strength" name="strength" 
                                    value="1.0" min="0.0" max="1.0" step="0.1">
                                <div class="range-value">1.0</div>
                            </div>
                            <div class="form-group">
                                <label for="rtc_image_seed">Seed</label>
                                <input type="number" class="form-control" id="rtc_image_seed" name="image_seed" value="0" min="-1">
                            </div>
                            <div class="form-group">
                                <label for="rtc_style_name">Style</label>
                                <select class="form-control" id="rtc_style_name" name="style_name"></select>
                            </div>
                            <button type="submit" class="btn">Generate</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="rt-canvas-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Outpaint -->
        <div id="image-outpaint" class="tab-content">
            <div class="page-container">
                <div class="page-sidebar">
                    <div class="card">
                        <form id="image-outpaint-form">
                            <div class="form-group">
                                <label for="op_image">Source Image</label>
                                <div class="dropzone" id="op_image_dropzone">
                                    <input type="file" id="op_image" name="image" accept="image/*" required hidden>
                                    <div class="dropzone-content">
                                        <span>Drop your image here or click to upload</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="op_image_size">Size</label>
                                <select class="form-control" id="op_image_size" name="image_size"></select>
                            </div>
                            <button type="submit" class="btn">Outpaint</button>
                        </form>
                    </div>
                </div>
                <div class="page-main">
                    <div class="card page-results">
                        <div class="gallery" id="image-outpaint-results"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- API Documentation -->
        <div id="api-docs" class="tab-content">
            <div class="page-container api-docs-container">
                <div class="card">
                    <div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">
                        <button class="btn" onclick="switchApiTab('inference')" id="inference-tab-btn">Inference Endpoints</button>
                        <button class="btn btn-secondary" onclick="switchApiTab('data')" id="data-tab-btn">Data Endpoints</button>
                    </div>

                    <div id="inference-endpoints" class="api-section">
                        <div style="overflow-x: auto;">
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 1.5rem;">
                                <thead>
                                    <tr>
                                        <th style="text-align: left; padding: 0.75rem; border-bottom: 1px solid var(--accent);">POST Endpoints</th>
                                        <th style="text-align: left; padding: 0.75rem; border-bottom: 1px solid var(--accent);">Description</th>
                                        <th style="text-align: left; padding: 0.75rem; border-bottom: 1px solid var(--accent);">Parameters</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- POST endpoints will be populated here -->
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <div id="data-endpoints" class="api-section" style="display: none;">
                        <div style="overflow-x: auto;">
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 1.5rem;">
                                <thead>
                                    <tr>
                                        <th style="text-align: left; padding: 0.75rem; border-bottom: 1px solid var(--accent);">GET Endpoints</th>
                                        <th style="text-align: left; padding: 0.75rem; border-bottom: 1px solid var(--accent);">Description</th>
                                        <th style="text-align: left; padding: 0.75rem; border-bottom: 1px solid var(--accent);">Response</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- GET endpoints will be populated here -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Update modal HTML -->
    <div id="image-preview-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <div class="modal-title">Image Preview</div>
                <button class="modal-close" aria-label="Close preview">×</button>
            </div>
            <div class="modal-body">
                <img class="modal-image" src="" alt="Preview">
            </div>
            <div class="modal-actions">
                <button class="modal-btn modal-download">
                    <i class="fas fa-download"></i>
                    Download
                </button>
                <button class="modal-btn modal-copy">
                    <i class="fas fa-copy"></i>
                    Copy to Clipboard
                </button>
            </div>
        </div>
    </div>

    <script>
        // Fetch available options from API endpoints
        async function fetchOptions() {
            try {
                const endpoints = {
                    models: '/v1/api/get/models',
                    modelsGuide: '/v1/api/get/models/guide',
                    modelsSvi: '/v1/api/get/models/svi',
                    modelsRemix: '/v1/api/get/models/remix',
                    styles: '/v1/api/get/styles',
                    sizes: '/v1/api/get/size',
                    loraSvi: '/v1/api/get/lora/svi',
                    loraFlux: '/v1/api/get/lora/flux',
                    loraRt: '/v1/api/get/lora/rt',
                    controlnets: '/v1/api/get/controlnets',
                    gfpgan: '/v1/api/get/gfpgan',
                    guideVariation: '/v1/api/get/guide/variation',
                    guideStructure: '/v1/api/get/guide/structure',
                    guideFacial: '/v1/api/get/guide/facial',
                    guideStyle: '/v1/api/get/guide/style'
                };

                const responses = await Promise.all(
                    Object.entries(endpoints).map(([key, url]) => 
                        fetch(url)
                            .then(r => r.json())
                            .catch(error => {
                                console.error(`Error fetching ${key}:`, error);
                                return null;
                            })
                    )
                );

                const data = Object.fromEntries(
                    Object.keys(endpoints).map((key, index) => [key, responses[index]])
                );

                // Populate standard model dropdowns
                ['model_name', 'var_model_name'].forEach(id => {
                    populateSelect(id, data.models?.models || []);
                });

                // Populate guide model dropdowns
                ['str_model_name', 'fac_model_name', 'sty_model_name'].forEach(id => {
                    populateSelect(id, data.modelsSvi?.models || []);
                });

                // Populate controlnet model dropdown
                populateSelect('cn_model_name', data.modelsRemix?.remix || []);

                // Populate style dropdowns
                [
                    'style_name', 'trans_style_name', 'var_style_name', 'str_style_name',
                    'fac_style_name', 'sty_style_name', 'cn_style_name', 'enh_style_name',
                    'gf_style_name', 'rtg_style_name', 'rtc_style_name'
                ].forEach(id => {
                    populateSelect(id, data.styles?.styles || []);
                });

                // Populate size dropdowns
                [
                    'image_size', 'trans_image_size', 'var_image_size', 'str_image_size',
                    'fac_image_size', 'sty_image_size', 'rtg_image_size', 'op_image_size'
                ].forEach(id => {
                    populateSelect(id, data.sizes?.size || []);
                });

                // Populate LoRA dropdowns
                ['lora_svi', 'var_lora_svi', 'str_lora_svi', 'fac_lora_svi', 'sty_lora_svi'].forEach(id => {
                    populateSelect(id, data.loraSvi?.models || []);
                });

                ['lora_flux', 'var_lora_flux'].forEach(id => {
                    populateSelect(id, data.loraFlux?.models || []);
                });

                ['rtg_lora', 'rtc_lora'].forEach(id => {
                    populateSelect(id, data.loraRt?.models || []);
                });

                // Populate controlnet dropdown
                populateSelect('cn_controlnet', data.controlnets?.controlnets || []);

                // Populate guide strength dropdowns
                populateSelect('var_strength', data.guideVariation?.variation || []);
                populateSelect('str_strength', data.guideStructure?.structure || []);
                populateSelect('fac_strength', data.guideFacial?.facial || []);
                populateSelect('sty_strength', data.guideStyle?.style || []);

                // Populate GFPGAN version dropdown
                populateSelect('tk_gfpgan_version', data.gfpgan?.gfpgan || []);

            } catch (error) {
                console.error('Error fetching options:', error);
            }
        }

        function populateSelect(id, options) {
            const select = document.getElementById(id);
            if (!select || !Array.isArray(options)) return;

            // Clear existing options
            select.innerHTML = '';

            // Add new options
            options.forEach(option => {
                const opt = document.createElement('option');
                opt.value = option;
                opt.textContent = option;
                select.appendChild(opt);
            });

            // Select first option by default
            if (options.length > 0) {
                select.value = options[0];
            }
        }

        // Page state management
        function savePageState() {
            const activeTab = document.querySelector('.nav-item.active').dataset.tab;
            localStorage.setItem('activeTab', activeTab);
        }

        function loadPageState() {
            const activeTab = localStorage.getItem('activeTab');
            if (activeTab) {
                document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                
                const tab = document.querySelector(`.nav-item[data-tab="${activeTab}"]`);
                if (tab) {
                    tab.classList.add('active');
                    document.getElementById(activeTab).classList.add('active');
                }
            }
        }

        // Unsaved changes warning
        let hasUnsavedChanges = false;

        function showUnsavedWarning() {
            // Removed the warning dialog functionality
            hasUnsavedChanges = true;
        }

        // Monitor form changes
        document.querySelectorAll('form').forEach(form => {
            form.addEventListener('change', () => {
                hasUnsavedChanges = true;
            });
            form.addEventListener('submit', () => {
                hasUnsavedChanges = false;
            });
        });

        // Remove beforeunload warning
        window.removeEventListener('beforeunload', () => {});

        // Tab handling
        document.querySelectorAll('.nav-item').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                
                tab.classList.add('active');
                document.getElementById(tab.dataset.tab).classList.add('active');
                savePageState();
            });
        });

        // Error handling function
        function showError(message) {
            const popup = document.createElement('div');
            popup.className = 'error-popup';
            
            const text = document.createElement('span');
            text.textContent = message;
            
            const closeBtn = document.createElement('button');
            closeBtn.className = 'close';
            closeBtn.innerHTML = '×';
            closeBtn.addEventListener('click', () => {
                popup.remove();
            });
            
            popup.appendChild(text);
            popup.appendChild(closeBtn);
            document.body.appendChild(popup);
            
            // Auto remove after 5 seconds
            setTimeout(() => {
                if (document.body.contains(popup)) {
                    popup.remove();
                }
            }, 5000);
        }

        // Update button state function
        function setButtonLoading(button, isLoading) {
            if (isLoading) {
                if (!button.dataset.originalText) {
                    button.dataset.originalText = button.innerHTML;
                }
                button.classList.add('loading');
                button.disabled = true;
            } else {
                button.classList.remove('loading');
                button.disabled = false;
                if (button.dataset.originalText) {
                    button.innerHTML = button.dataset.originalText;
                }
            }
        }

        // Form handling for Image Toolkit
        document.getElementById('tk_gfpgan').addEventListener('click', async () => {
            const button = document.getElementById('tk_gfpgan');
            const form = document.getElementById('image-toolkit-form');
            const formData = new FormData(form);
            formData.append('model_version', document.getElementById('tk_gfpgan_version').value);
            
            try {
                setButtonLoading(button, true);
                const response = await fetch('/v1/api/face/gfpgan', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                if (data.success) {
                    updateGallery('image-toolkit-results', data.result);
                } else {
                    showError(data.error || 'Failed to process image with GFPGAN');
                }
            } catch (error) {
                console.error('Error in GFPGAN:', error);
                showError('Failed to connect to the server');
            } finally {
                setButtonLoading(button, false);
            }
        });

        document.getElementById('tk_codeformer').addEventListener('click', async () => {
            const button = document.getElementById('tk_codeformer');
            const form = document.getElementById('image-toolkit-form');
            const formData = new FormData(form);
            
            try {
                setButtonLoading(button, true);
                const response = await fetch('/v1/api/face/codeformer', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                if (data.success) {
                    updateGallery('image-toolkit-results', data.result);
                } else {
                    showError(data.error || 'Failed to process image with CodeFormer');
                }
            } catch (error) {
                console.error('Error in CodeFormer:', error);
                showError('Failed to connect to the server');
            } finally {
                setButtonLoading(button, false);
            }
        });

        document.getElementById('tk_upscale').addEventListener('click', async () => {
            const form = document.getElementById('image-toolkit-form');
            const formData = new FormData(form);
            
            try {
                const response = await fetch('/v1/api/image/upscale', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                if (data.success) {
                    updateGallery('image-toolkit-results', data.result);
                }
            } catch (error) {
                console.error('Error in upscaling:', error);
            }
        });

        document.getElementById('tk_bgremove').addEventListener('click', async () => {
            const form = document.getElementById('image-toolkit-form');
            const formData = new FormData(form);
            
            try {
                const response = await fetch('/v1/api/image/bgremove', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                if (data.success) {
                    updateGallery('image-toolkit-results', data.result);
                }
            } catch (error) {
                console.error('Error in background removal:', error);
            }
        });

        document.getElementById('tk_caption').addEventListener('click', async () => {
            const form = document.getElementById('image-toolkit-form');
            const formData = new FormData(form);
            
            try {
                const response = await fetch('/v1/api/image/caption', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                if (data.success) {
                    document.getElementById('tk_caption_result').value = data.result;
                }
            } catch (error) {
                console.error('Error in captioning:', error);
            }
        });

        document.getElementById('tk_prompt').addEventListener('click', async () => {
            const form = document.getElementById('image-toolkit-form');
            const formData = new FormData(form);
            
            try {
                const response = await fetch('/v1/api/image/prompt', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                if (data.success) {
                    document.getElementById('tk_prompt_result').value = data.result;
                }
            } catch (error) {
                console.error('Error in prompt generation:', error);
            }
        });

        // Helper function to update gallery
        function updateGallery(galleryId, imageUrl) {
            const gallery = document.getElementById(galleryId);
            const form = document.querySelector(`#${galleryId.replace('-results', '-form')}`);
            const prompt = form.querySelector('textarea[name="prompt"]')?.value || 'No prompt';

            // Find or create row for this prompt
            let row = Array.from(gallery.children).find(row => 
                row.dataset.prompt === prompt && 
                row.dataset.timestamp === form.dataset.lastSubmitTime
            );

            // If no row exists or prompt was resubmitted, create new row
            if (!row) {
                row = document.createElement('div');
                row.className = 'gallery-row';
                row.dataset.prompt = prompt;
                row.dataset.timestamp = Date.now();
                form.dataset.lastSubmitTime = row.dataset.timestamp;

                // Create header with prompt and copy button
                const header = document.createElement('div');
                header.className = 'gallery-row-header';

                const title = document.createElement('div');
                title.className = 'gallery-row-title';
                title.textContent = prompt;

                const copyBtn = document.createElement('button');
                copyBtn.className = 'gallery-row-copy';
                copyBtn.innerHTML = '<i class="fas fa-copy"></i> Copy';
                copyBtn.addEventListener('click', () => {
                    navigator.clipboard.writeText(prompt);
                    copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied';
                    setTimeout(() => {
                        copyBtn.innerHTML = '<i class="fas fa-copy"></i> Copy';
                    }, 2000);
                });

                header.appendChild(title);
                header.appendChild(copyBtn);
                row.appendChild(header);

                // Create container for images
                const imagesContainer = document.createElement('div');
                imagesContainer.className = 'gallery-row-images';
                row.appendChild(imagesContainer);

                // Insert at the beginning of the gallery
                gallery.insertBefore(row, gallery.firstChild);
            }

            // Create gallery item
            const item = document.createElement('div');
            item.className = 'gallery-item';
            
            const img = document.createElement('img');
            img.src = imageUrl;
            img.alt = 'Generated image';
            
            const actions = document.createElement('div');
            actions.className = 'actions';
            
            const previewBtn = document.createElement('button');
            previewBtn.className = 'action-btn preview-btn';
            previewBtn.innerHTML = '<i class="fas fa-eye"></i>';
            previewBtn.title = 'Preview';
            previewBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                openImagePreview(imageUrl);
            });
            
            const downloadBtn = document.createElement('button');
            downloadBtn.className = 'action-btn download-btn';
            downloadBtn.innerHTML = '<i class="fas fa-download"></i>';
            downloadBtn.title = 'Download';
            downloadBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                downloadImage(imageUrl);
            });
            
            actions.appendChild(previewBtn);
            actions.appendChild(downloadBtn);
            
            item.appendChild(img);
            item.appendChild(actions);
            
            // Add click event for preview
            item.addEventListener('click', () => openImagePreview(imageUrl));
            
            // Add to the images container at the beginning
            const imagesContainer = row.querySelector('.gallery-row-images');
            imagesContainer.insertBefore(item, imagesContainer.firstChild);
        }

        // Update image preview functionality
        const modal = document.getElementById('image-preview-modal');
        const modalImage = modal.querySelector('.modal-image');
        const modalClose = modal.querySelector('.modal-close');
        const modalDownload = modal.querySelector('.modal-download');
        const modalCopy = modal.querySelector('.modal-copy');

        function openImagePreview(imageUrl) {
            modalImage.src = imageUrl;
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeImagePreview() {
            modal.classList.remove('active');
            document.body.style.overflow = '';
            modalImage.src = '';
        }

        modalClose.addEventListener('click', closeImagePreview);
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeImagePreview();
        });

        modalDownload.addEventListener('click', () => {
            if (modalImage.src) {
                downloadImage(modalImage.src);
            }
        });

        modalCopy.addEventListener('click', async () => {
            try {
                const response = await fetch(modalImage.src);
                const blob = await response.blob();
                await navigator.clipboard.write([
                    new ClipboardItem({
                        [blob.type]: blob
                    })
                ]);
                
                const originalText = modalCopy.innerHTML;
                modalCopy.innerHTML = '<i class="fas fa-check"></i> Copied!';
                setTimeout(() => {
                    modalCopy.innerHTML = originalText;
                }, 2000);
            } catch (error) {
                console.error('Error copying image:', error);
            }
        });

        // Handle escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeImagePreview();
            }
        });

        // Download functionality
        async function downloadImage(imageUrl) {
            try {
                const response = await fetch(imageUrl);
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `generated-image-${Date.now()}.webp`;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                document.body.removeChild(a);
            } catch (error) {
                console.error('Error downloading image:', error);
            }
        }

        // Form handling for all other forms
        const formEndpoints = {
            'image-generator-form': '/v1/api/image/generate',
            'transparent-generator-form': '/v1/api/image/transparent',
            'image-variation-form': '/v1/api/image/variation',
            'image-structure-form': '/v1/api/image/structure',
            'image-facial-form': '/v1/api/image/facial',
            'image-style-form': '/v1/api/image/style',
            'image-controlnet-form': '/v1/api/image/controlnet',
            'image-enhance-form': '/v1/api/image/enhance',
            'object-eraser-form': '/v1/api/image/erase',
            'generative-fill-form': '/v1/api/image/inpaint',
            'rt-generator-form': '/v1/api/realtime/generate',
            'rt-canvas-form': '/v1/api/realtime/canvas',
            'image-outpaint-form': '/v1/api/image/outpaint'
        };

        Object.entries(formEndpoints).forEach(([formId, endpoint]) => {
            document.getElementById(formId).addEventListener('submit', async (e) => {
                e.preventDefault();
                const form = e.target;
                const button = form.querySelector('button[type="submit"]');
                const formData = new FormData(form);
                const resultGalleryId = formId.replace('-form', '-results');
                
                try {
                    setButtonLoading(button, true);
                    
                    const response = await fetch(endpoint, {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    if (data.success) {
                        updateGallery(resultGalleryId, data.result);
                    } else {
                        showError(data.error || 'Failed to process request');
                    }
                } catch (error) {
                    console.error(`Error in ${formId}:`, error);
                    showError('Failed to connect to the server');
                } finally {
                    setButtonLoading(button, false);
                }
            });
        });

        // Initialize
        fetchOptions();
        loadPageState();
        wrapCheckboxes();

        // Dropzone functionality
        document.querySelectorAll('.dropzone').forEach(dropzone => {
            const input = dropzone.querySelector('input[type="file"]');
            const content = dropzone.querySelector('.dropzone-content');

            dropzone.addEventListener('click', () => input.click());
            dropzone.addEventListener('dragover', e => {
                e.preventDefault();
                dropzone.classList.add('dragover');
            });
            dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
            dropzone.addEventListener('drop', e => {
                e.preventDefault();
                dropzone.classList.remove('dragover');
                input.files = e.dataTransfer.files;
                input.dispatchEvent(new Event('change'));
            });

            input.addEventListener('change', () => {
                if (input.files.length > 0) {
                    content.textContent = input.files[0].name;
                    const url = URL.createObjectURL(input.files[0]);
                    dropzone.style.backgroundImage = `url(${url})`;
                    content.style.display = 'none';
                } else {
                    content.textContent = 'Drop your image here or click to upload';
                    dropzone.style.backgroundImage = 'none';
                    content.style.display = 'block';
                }
            });
        });

        // Add JavaScript for range input value updates
        document.querySelectorAll('input[type="range"]').forEach(range => {
            const valueDisplay = range.parentElement.querySelector('.range-value');
            range.addEventListener('input', () => {
                valueDisplay.textContent = range.value + (range.id.includes('strength') ? '%' : '');
            });
        });

        // Update all checkbox wrappers
        function wrapCheckboxes() {
            document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
                if (!checkbox.closest('.checkbox-wrapper')) {
                    const labelText = checkbox.closest('label')?.textContent.trim() || 
                                    checkbox.nextSibling?.textContent.trim() || '';
                    
                    // Create new wrapper
                    const wrapper = document.createElement('label');
                    wrapper.className = 'checkbox-wrapper';
                    
                    // Move checkbox into wrapper
                    checkbox.parentElement.insertBefore(wrapper, checkbox);
                    wrapper.appendChild(checkbox);
                    
                    // Add label text
                    const span = document.createElement('span');
                    span.textContent = labelText;
                    wrapper.appendChild(span);
                    
                    // Remove old label or text node
                    if (checkbox.nextSibling?.nodeType === Node.TEXT_NODE) {
                        checkbox.nextSibling.remove();
                    }
                    const oldLabel = checkbox.closest('label:not(.checkbox-wrapper)');
                    if (oldLabel) {
                        oldLabel.replaceWith(wrapper);
                    }
                }
            });
        }

        // API Documentation tab switching
        function switchApiTab(tab) {
            const inferenceSection = document.getElementById('inference-endpoints');
            const dataSection = document.getElementById('data-endpoints');
            const inferenceBtn = document.getElementById('inference-tab-btn');
            const dataBtn = document.getElementById('data-tab-btn');

            if (tab === 'inference') {
                inferenceSection.style.display = 'block';
                dataSection.style.display = 'none';
                inferenceBtn.classList.remove('btn-secondary');
                dataBtn.classList.add('btn-secondary');
            } else {
                inferenceSection.style.display = 'none';
                dataSection.style.display = 'block';
                inferenceBtn.classList.add('btn-secondary');
                dataBtn.classList.remove('btn-secondary');
            }
        }

        // Populate API documentation tables
        function populateApiDocs() {
            const inferenceEndpoints = [
                {
                    endpoint: '/v1/api/image/generate',
                    description: 'Generate images from text prompts',
                    params: [
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'model_name: Model name (default: "flux-turbo")',
                        'image_size: Size ratio (default: "1:1")',
                        'lora_svi: LoRA SVI preset',
                        'lora_flux: LoRA Flux preset',
                        'image_seed: Generation seed',
                        'style_name: Style preset',
                        'enhance_prompt: Enable prompt enhancement'
                    ]
                },
                {
                    endpoint: '/v1/api/image/transparent',
                    description: 'Generate images with transparent backgrounds',
                    params: [
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'image_size: Size ratio (default: "1:1")',
                        'image_seed: Generation seed',
                        'style_name: Style preset',
                        'enhance_prompt: Enable prompt enhancement',
                        'transparent: Enable transparent image (default: true)'
                    ]
                },
                {
                    endpoint: '/v1/api/image/variation',
                    description: 'Create variations of existing images',
                    params: [
                        'image (required): Source image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'model_name: Model name (default: "flux-turbo")',
                        'image_size: Size ratio (default: "1:1")',
                        'strength: Variation strength',
                        'lora_svi: LoRA SVI preset',
                        'lora_flux: LoRA Flux preset',
                        'image_seed: Generation seed',
                        'style_name: Style preset',
                        'enhance_prompt: Enable prompt enhancement'
                    ]
                },
                {
                    endpoint: '/v1/api/image/structure',
                    description: 'Apply structural guidance to images',
                    params: [
                        'image (required): Source image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'model_name: Model name (default: "svi-realistic")',
                        'image_size: Size ratio (default: "1:1")',
                        'strength: Guidance strength',
                        'lora_svi: LoRA SVI preset',
                        'image_seed: Generation seed',
                        'style_name: Style preset',
                        'enhance_prompt: Enable prompt enhancement'
                    ]
                },
                {
                    endpoint: '/v1/api/image/facial',
                    description: 'Apply facial guidance to images',
                    params: [
                        'image (required): Source image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'model_name: Model name (default: "svi-realistic")',
                        'image_size: Size ratio (default: "1:1")',
                        'strength: Guidance strength',
                        'lora_svi: LoRA SVI preset',
                        'image_seed: Generation seed',
                        'style_name: Style preset',
                        'enhance_prompt: Enable prompt enhancement'
                    ]
                },
                {
                    endpoint: '/v1/api/image/style',
                    description: 'Apply style guidance to images',
                    params: [
                        'image (required): Source image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'model_name: Model name (default: "svi-realistic")',
                        'image_size: Size ratio (default: "1:1")',
                        'strength: Style strength',
                        'lora_svi: LoRA SVI preset',
                        'image_seed: Generation seed',
                        'style_name: Style preset',
                        'enhance_prompt: Enable prompt enhancement'
                    ]
                },
                {
                    endpoint: '/v1/api/image/outpaint',
                    description: 'Extend images beyond their borders',
                    params: [
                        'image (required): Source image',
                        'image_size: Size ratio (default: "16:9")'
                    ]
                },
                {
                    endpoint: '/v1/api/realtime/canvas',
                    description: 'Real-time canvas processing',
                    params: [
                        'image (required): Source image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'lora_rt: LoRA RT preset',
                        'strength: Creativity level (default: 0.9)',
                        'image_seed: Generation seed',
                        'style_name: Style preset'
                    ]
                },
                {
                    endpoint: '/v1/api/realtime/generate',
                    description: 'Real-time image generation',
                    params: [
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'image_size: Size ratio (default: "1:1")',
                        'lora_rt: LoRA RT preset',
                        'image_seed: Generation seed',
                        'style_name: Style preset'
                    ]
                },
                {
                    endpoint: '/v1/api/image/inpaint',
                    description: 'Fill masked areas in images',
                    params: [
                        'image (required): Source image',
                        'mask (required): Mask image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'strength: Inpainting strength (default: 0.5)',
                        'cfg: Prompt scale (default: 9.0)',
                        'style_name: Style preset'
                    ]
                },
                {
                    endpoint: '/v1/api/image/erase',
                    description: 'Remove content from masked areas',
                    params: [
                        'image (required): Source image',
                        'mask (required): Mask image',
                        'cfg: Prompt scale (default: 9.0)'
                    ]
                },
                {
                    endpoint: '/v1/api/image/enhance',
                    description: 'Enhance image quality',
                    params: [
                        'image (required): Source image',
                        'prompt: Text prompt',
                        'negative_prompt: Negative prompt',
                        'creativity: Creativity level (default: 0.3)',
                        'resemblance: Resemblance level (default: 1)',
                        'hdr: HDR strength (default: 0)',
                        'style_name: Style preset'
                    ]
                },
                {
                    endpoint: '/v1/api/image/controlnet',
                    description: 'Apply ControlNet guidance',
                    params: [
                        'image (required): Source image',
                        'prompt (required): Text prompt',
                        'negative_prompt: Negative prompt',
                        'model_name: Model name (default: "sd-toon")',
                        'controlnet: Control type (default: "scribble")',
                        'strength: Control strength (default: 70)',
                        'cfg: Prompt scale (default: 9.0)',
                        'image_seed: Generation seed',
                        'style_name: Style preset'
                    ]
                },
                {
                    endpoint: '/v1/api/face/gfpgan',
                    description: 'Face restoration using GFPGAN',
                    params: [
                        'image (required): Source image',
                        'model_version: Model version (default: "1.3")'
                    ]
                },
                {
                    endpoint: '/v1/api/face/codeformer',
                    description: 'Face restoration using CodeFormer',
                    params: [
                        'image (required): Source image'
                    ]
                },
                {
                    endpoint: '/v1/api/image/upscale',
                    description: 'Upscale image resolution',
                    params: [
                        'image (required): Source image'
                    ]
                },
                {
                    endpoint: '/v1/api/image/bgremove',
                    description: 'Remove image background',
                    params: [
                        'image (required): Source image'
                    ]
                },
                {
                    endpoint: '/v1/api/image/caption',
                    description: 'Generate image captions',
                    params: [
                        'image (required): Source image'
                    ]
                },
                {
                    endpoint: '/v1/api/image/prompt',
                    description: 'Generate prompts from images',
                    params: [
                        'image (required): Source image'
                    ]
                },
                {
                    endpoint: '/v1/api/image/size',
                    description: 'Get aspect ratio and resolution of images',
                    params: [
                        'image (required): Source image'
                    ]
                }
            ];

            const dataEndpoints = [
                {
                    endpoint: '/v1/api/get/models',
                    description: 'List all available models',
                    response: ['models: List of model names']
                },
                {
                    endpoint: '/v1/api/get/models/guide',
                    description: 'List guidance models',
                    response: ['models: List of guidance model names']
                },
                {
                    endpoint: '/v1/api/get/models/flux',
                    description: 'List Flux models',
                    response: ['models: List of Flux model names']
                },
                {
                    endpoint: '/v1/api/get/models/svi',
                    description: 'List SVI models',
                    response: ['models: List of SVI model names']
                },
                {
                    endpoint: '/v1/api/get/models/sdxl',
                    description: 'List SDXL models',
                    response: ['models: List of SDXL model names']
                },
                {
                    endpoint: '/v1/api/get/models/remix',
                    description: 'List Remix models',
                    response: ['remix: List of Remix model names']
                },
                {
                    endpoint: '/v1/api/get/lora/flux',
                    description: 'List Flux LoRA presets',
                    response: ['models: List of Flux LoRA presets']
                },
                {
                    endpoint: '/v1/api/get/lora/svi',
                    description: 'List SVI LoRA presets',
                    response: ['models: List of SVI LoRA presets']
                },
                {
                    endpoint: '/v1/api/get/lora/rt',
                    description: 'List RT LoRA presets',
                    response: ['models: List of RT LoRA presets']
                },
                {
                    endpoint: '/v1/api/get/styles',
                    description: 'List style presets',
                    response: ['styles: List of style presets']
                },
                {
                    endpoint: '/v1/api/get/controlnets',
                    description: 'List ControlNet types',
                    response: ['controlnets: List of ControlNet types']
                },
                {
                    endpoint: '/v1/api/get/gfpgan',
                    description: 'List GFPGAN versions',
                    response: ['gfpgan: List of GFPGAN versions']
                },
                {
                    endpoint: '/v1/api/get/size',
                    description: 'List available size ratios',
                    response: ['size: List of size ratios']
                },
                {
                    endpoint: '/v1/api/get/guide/variation',
                    description: 'List variation strength ranges',
                    response: ['variation: Variation strength range']
                },
                {
                    endpoint: '/v1/api/get/guide/structure',
                    description: 'List structure guidance ranges',
                    response: ['structure: Structure guidance range']
                },
                {
                    endpoint: '/v1/api/get/guide/facial',
                    description: 'List facial guidance ranges',
                    response: ['facial: Facial guidance range']
                },
                {
                    endpoint: '/v1/api/get/guide/style',
                    description: 'List style guidance ranges',
                    response: ['style: Style guidance range']
                }
            ];

            // Populate inference endpoints
            const inferenceTable = document.querySelector('#inference-endpoints tbody');
            inferenceEndpoints.forEach(endpoint => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${endpoint.endpoint}</td>
                    <td>${endpoint.description}</td>
                    <td><ul>${endpoint.params.map(p => `<li><code>${p}</code></li>`).join('')}</ul></td>
                `;
                inferenceTable.appendChild(row);
            });

            // Populate data endpoints
            const dataTable = document.querySelector('#data-endpoints tbody');
            dataEndpoints.forEach(endpoint => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${endpoint.endpoint}</td>
                    <td>${endpoint.description}</td>
                    <td><ul>${endpoint.response.map(r => `<li><code>${r}</code></li>`).join('')}</ul></td>
                `;
                dataTable.appendChild(row);
            });
        }

        // Call populateApiDocs after the page loads
        document.addEventListener('DOMContentLoaded', populateApiDocs);

        // Add validation for seed inputs
        document.querySelectorAll('input[type="number"][name="image_seed"]').forEach(input => {
            input.addEventListener('change', (e) => {
                const value = parseInt(e.target.value);
                if (value < -1) {
                    e.target.value = -1;
                }
            });
        });
    </script>
</body>
</html>
