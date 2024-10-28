using System;
using System.IO;
using System.Net;
using System.Text;

class AvoSecurity
{
    static void Main(string[] args)
    {
        Console.WriteLine("Welcome to Avo Security!");
        
        // Путь к каталогу для проверки
        string directoryToScan = @"C:\path\to\scan";
        ScanDirectory(directoryToScan);

        // Блокировка доступа к плохим сайтам
        BlockBadWebsites();
    }

    static void ScanDirectory(string path)
    {
        Console.WriteLine($"Scanning directory: {path}");

        // Пример списка вредоносных файлов (в реальной программе используйте более обширный список)
        string[] maliciousFiles = { "malware.exe", "virus.bat", "ransomware.scr" };

        foreach (var file in Directory.GetFiles(path))
        {
            string fileName = Path.GetFileName(file);
            if (Array.Exists(maliciousFiles, element => element == fileName))
            {
                Console.WriteLine($"Malicious file found: {fileName}. Deleting...");
                File.Delete(file);
            }
        }
    }

    static void BlockBadWebsites()
    {
        // Пример списка плохих сайтов
        string[] badWebsites = { "badwebsite.com", "malicious-site.org" };

        Console.WriteLine("Blocking access to bad websites...");

        foreach (var site in badWebsites)
        {
            Console.WriteLine($"Blocking: {site}");
            // Здесь можно добавить логику блокировки (например, редактирование hosts файла)
            BlockWebsite(site);
        }
    }

    static void BlockWebsite(string website)
    {
        // Пример редактирования файла hosts (для Windows)
        string hostsFilePath = @"C:\Windows\System32\drivers\etc\hosts";

        try
        {
            using (StreamWriter sw = File.AppendText(hostsFilePath))
            {
                sw.WriteLine($"127.0.0.1 {website}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error blocking website {website}: {ex.Message}");
        }
    }
}
